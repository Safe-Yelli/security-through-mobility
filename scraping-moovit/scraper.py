from bs4 import BeautifulSoup as bs
import traceback
import requests
import os
import pandas as pd
import glob
import sys

def findBusRoutes(searchLink):
    routes = []  
    routeNumber = []
    route = []
    routeStopsLink = []
    
    # Get page content
    try:
        pageContent = requests.get(searchLink).content
    except Exception:
        traceback.print_exc

    # Parse and find all routeNumbers and routes
    parseContent = bs(pageContent, 'lxml')
    routeNumberUnParsed = parseContent.find(id="agency-lines").find_all(class_= "transit-icon-bus")
    routeUnParsed = parseContent.find(id="agency-lines").find_all(class_="line-title")
    routeStopsLinkUnParsed = parseContent.find(id="agency-lines").findAll('a')


    # Parse and find attrs

    for rstop in routeStopsLinkUnParsed:
        routeStopsLink.append(rstop['href'])
    
    for rNm in routeNumberUnParsed:
        routeNumber.append(rNm['alt'])
    
    for r in routeUnParsed:
        route.append(r.text)

    
    # Write to csv
    try:
        filePath = os.path.join(path, "test.csv")
        routes = pd.DataFrame(list(zip(routeNumber, route, routeStopsLink)))
        routes.to_csv(filePath)

    except Exception:
        traceback.print_exc()
        print("Issue with link")

    return routes

def main():

    # Path to write to
    global path 
    path = 'routes'
    if not os.path.exists(path):
        os.makedirs(path)

    # Link to scrape from
    searchLink = "https://moovitapp.com/index/en/public_transit-lines-Bengaluru-3620-2005263"

    findBusRoutes(searchLink)

main()