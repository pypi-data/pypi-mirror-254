#!/usr/bin/env python3

import re
import os
import json
import click
import httpx
from tqdm import tqdm
from tabulate import tabulate

from csv import writer as writer
from collections import defaultdict
from keyring import get_password, set_password, delete_password

__author__ = "Muhamed Qasim"
__version__ = "0.1.0"


def highlight(string:str, word:str) -> str:
   # index matched word
   wlen = len(word)
   indx = string.lower().index(word.lower())
   # take matched line
   for string in string.splitlines():
      if word in string : break
   # remove tap spaces
   string = string.replace("\t", " ")
   # shortcuting string
   if wlen+indx > 45 :
      frm = indx      - (50//2)
      end = indx+wlen + (50//2)
   else:
      frm = 0
      end = 50
   # get shortcut and heighlight matched string
   string = "".join([
      string[frm:indx],           # from pos to matched word
      "\033[1;31m",                 # start color
      string[indx:indx+wlen],     # from word to end word
      "\033[0m",                  # end color
      string[indx+wlen:end]       # from end word to end
      ])
   return string



def find_matched_port(filters:dict, data:dict, hlight:bool) -> list:
   matchedlist = []
   for port in data["ports"] :
      cpes    = port.pop("cpe", [])
      scripts = port.pop("script", {}).values()
      matched = []
      for key, values in filters.items():
         key = key.lower()
         for value in values : # test many values like port:80,8080,..
            match key:
               case "country":
                  value = country.iso.get(value.lower(), value.title())
                  if hlight : data[key] = highlight(value, value)
               case "isp" | "city" | "org" | "zip" | "ip" :
                  if hlight : data[key] = highlight(data[key], value)
               case "service" | "product" |  "version" | "info" | "os" | "script" | "info" :
                  if value.lower() in port.get(key, ".").lower() :
                     matched.append(True)
                     if hlight : port[key] = highlight(port[key], value)
               case "port" :
                  if value == port.get(key, ".") :
                     matched.append(True)
                     if hlight : port[key] = highlight(value, value)
               case "cpe":
                  for cpe in cpes :
                     if value.lower() in cpe :
                        matched.append(True)
                        if hlight :
                           port["cpe"] = highlight(cpe, value)
                        break
               case "text" :
                  for key in ["port", "service", "product", "version", "info", "os", "script"]:
                     if value.lower() in port.get(key, ".").lower() :
                        matched.append(True)
                        if hlight : port[key] = highlight(port[key], value)
                        break
                  for key in ["org", "isp"]:
                     if value.lower() in data.get(key, ".").lower() :
                        if hlight : data[key] = highlight(data[key], value)
                        break


      if any(v in filters for v in ["port", "service", "product", "version", "info", "os"]):
         if any(matched):
            matchedlist.append(data | port)
      else:
         matchedlist.append(data | port)

   return matchedlist



def csv_writer_ip(csvwriter:writer, json:list, filters:dict, headers:list, no:int) -> None:
   rows = []
   for data in json:
      matchedlist = find_matched_port(filters, data, False)
      for matched in matchedlist:
         matched["no"] = str(no)
         row = [ matched.get(head, "")  for head in headers ]
         rows.append(row)
   csvwriter.writerows(rows)



def print_results(json:list, filters:dict, headers:list, no:int) -> None:
   table = []
   tee   = "├  "
   elbow = "└───"
   for data in json:
      no += 1
      perfix = tee
      matchedlist = find_matched_port(filters, data, True)
      if matchedlist:
         for matched in matchedlist:
            matched["no"] = perfix + str(no) if perfix == tee  else elbow
            row = [ matched.get(head, "")  for head in headers ]
            table.append(row)
            perfix = elbow
   if table :
      print(tabulate(table, headers=headers))
   else:
      print("Not Found!")


def print_stats(stats:list, headers:list) -> None:
   table = [["", "Total" , f"{stats.pop('total'):,}"]]
   for category, branch  in stats.items() :
      table.append([category, "", ""])
      for n, (name, value) in enumerate(branch.items()):
         category = "└───"
         table.append([category, name, f"{value:,}"])
         if n == 5 : break
   print(tabulate(table, headers=["headers", "name", "value"]))


def print_message(code:int) -> None:
   match code :
      case 401:
         print("Unauthorized - Your API key is not valid or missing.")
      case 402:
         print("Payment Requierd - Service unavailable in current subscription")
      case 410 :
         print("Service Unavailable - The service is currently unavailable. Please try again later.")
      case 429:
         print("Too Many Requests - You have reached the maximum number of requests.")
      case 500:
         print("Subscription Expired - please renew your subscription.")
      case 503:
         print("Internal Server Error - We encountered an unexpected error while processing yourrequest.")
      case 504 :
         print("Gateway Timeout - The server did not receive a timely response from an upstream server.")
      case _:
         print(f"{code} - Unknown error please contact tech support")



def search(filters:tuple, page:int, size:int, headers:str) -> None:
   params = defaultdict(list)
   if headers == "auto":
      headers = ["no", "ip", "port", "service", "product", "version", "os"]
      for filter in filters :
         key, value = filter.split(":")
         params[key].append(value)
         if not key in headers:
            headers.append(key)
   else:
      headers = headers.split(",")

   filters = dict(params)
   params["page"] = page
   params["size"] = size
   with create_client() as client :
      no = (page-1) * size
      response = client.get("/api/search", params=params)
      if response.status_code == 200 :
         print_results(response.json(), filters, headers, no)
      else:
         print_message(response.status_code)


def stats(filters:tuple) -> None:
   params = defaultdict(list)
   for filter in filters :
      key, value = filter.split(":")
      params[key].append(value)
   with create_client() as client :
      response = client.get("/api/stats", params=dict(params))
      if response.status_code == 200 :
         print_stats(response.json(), [])
      else:
         print_message(response.status_code)


def download(filters:tuple, headers:str, csv:str, size:int) -> None:
   params = defaultdict(list)
   if headers == "auto":
      headers = ["no", "ip", "port", "service", "product", "version", "os"]
      for filter in filters :
         key, value = filter.split(":")
         params[key].append(value)
         if not key in headers:
            headers.append(key)
   else:
      headers = headers.split(",")

   filters = dict(params)
   csvfile = open(file=csv, mode="w", newline="")

   with create_client() as client :
      response = client.get("/api/stats", params=params)
      if response.status_code == 200 :
         stats = response.json()

         if size == 0 :
            fullsize = stats["total"]
         else:
            fullsize = min(size, stats["total"])

         csvwriter = writer(csvfile)
         csvwriter.writerow(headers)
         no, page = 0, 1

         with tqdm(total=fullsize, desc="Downloading", unit="ip") as bar :
            for chunk in ([1000] * (fullsize//1000) ) + [fullsize%1000] :
               params["size"] = chunk
               params["page"] = page
               response = client.get("/api/search", params=params)
               if response.status_code == 200 :
                  csv_writer_ip(csvwriter, response.json(), filters, headers, no)
               else:
                  print_message(response.status_code)
                  break
               no   += chunk
               page += 1
               bar.update(chunk)
      else:
         print_message(response.status_code)

   csvfile.close()


def create_client() -> httpx.Client:
   transport = httpx.HTTPTransport(retries=5)
   client =  httpx.Client(
      base_url="https://anytarget.net",
      headers={"Content-Type": "application/json"},
      params={"apikey":get_password("anytarget", "APIKEY")},
      verify=False,
      transport=transport,
      )
   return client


########################################################


@click.group(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True))
def cli():
   """This is the main entry point for the CLI."""
   pass

@cli.command(name="search")#, context_settings=opt)
@click.argument("filters", required=True, nargs=-1 )
@click.option("-p", "--page", type=int, default=1, help="Used to specify the desired page of results when using paginated search. It's often used in conjunction with 'size to segment results into pages, page = [1,2,3,n] -> results = [n*size] && skip = [n*size]")
@click.option("-s", "--size", type=int, default=10, help= "The number of results retrieved in a single request. It determines the page size or the quantity the request should return.")
@click.option("-h", "--headers", type=str, default="auto", help="for example: no,ip,port,service,product,country")
def search_command(**kwargs):
   """Use the search command to retrieve specific results"""
   return search(**kwargs)

@cli.command(name="download")
@click.argument("filters", required=True, nargs=-1)
@click.option("-c","--csv", required=True,  type=click.Path(), help="csv file output")
@click.option("-h", "--headers", type=str, default="auto", help="for example: no,ip,port,service,product,country")
@click.option("-s","--size", required=False, type=int, default=0, help="The number of results downloaded use 0 to download all results.")
def download_command(**kwargs):
   """Use the download command to export results into a CSV file"""
   return download(**kwargs)

@cli.command(name="stats")
@click.argument("filters", required=True, nargs=-1)
def stats_command(**kwargs):
   """Use the stats command to obtain statistical information about the results"""
   return stats(**kwargs)

@cli.command(name="auth")
@click.argument("apikey", required=True, nargs=1)
def auth_command(apikey):
   """Initialize / Update API Accesss Key"""
   set_password("anytarget", "APIKEY", apikey)

@cli.command(name="rmauth")
def rmauth_command():
   """Remove your Accesss Key from this device"""
   delete_password("anytarget", "APIKEY")


