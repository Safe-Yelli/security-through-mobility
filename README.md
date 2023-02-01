
*Work in progress*
# Security *through* mobility, not just *in* mobility

**Link**: https://safe-yelli.github.io/security-through-mobility/
## Context
- Women face a lot of issues with accessibility through the lens of safety on roads. [^3]
    - SafeYelli [^4] has been documenting it for over a year. So have SafeCity [^5], SafetyPin [^6] and other solutions
- Safety and access to **public spaces in the city are negotiated for accessibility to the self by women** [^7]

### Motivations to design with
- **Crime Prevention Through Environment Design** (CPTED) is something that can be used to redesign bustands as safety islands as opposed to the City's initative to build safety islands  [^1]
- **Constant life and movement** should be encouraged by **mixed activites.** Bus Stands in India are already full of mixed activites, but can it be **formally encouraged**? [^2]
- **Feeder busses would encourage constant activity**. [Need Citation]
- A data visualisation to **realise the areas that are not covered by existing bus routes and would be helped by feeder busses. A system?** could be created. 
- What new methods exist to understanding a complex routing system? Through [SFNetworks](https://luukvdmeer.github.io/sfnetworks) and [STPlanner](https://github.com/ropensci/stplanr) packages for R.

## Problem statement
- Smaller or no Bus travel roads need to have busses running through them. Like on the inner roads of Ylk New Town.
- What are these roads that the BMTC needs to run new routes on?
    - Are they based on population density?
    - Are they based on the number of workplaces nearby?
    - Are there a lot of long distance travellers? Do migrants stay in housing that is far away?
    - Are these roads deserted after a certain time?

## Avant-garde routing
- What if i ignore residential zoning and route public transport through them.
- Would this not reduce private vehicle traffic possibly?


## Analysing the network
### Algorithm as i see it
- Load both layers (Bus routes and existing network)
- Find intersecting roads or roads that satisfy a filter within a radius
    - Filter out roads that do not have a bus route
      - Filter/Weight based on population, school density, work-place density, etc

## Learning history 
- Multiple CRS issues the busRoutes and RoadNetwork data come from different sources
- Both networks are not fully alike and hence the network cannot be analysed without fully snapping both networks together. 
  - I attempted to round the data to achieve this, but this does not fully work. 
  - I need to snap with the sf library's method, did not work and could not fully implement in the given time
  - The edge query functions need to be fully explored
## To be done
- Implement multiple other filters as suggested previously
- Simplify and round both networks
- Verify idea with professionals

 [^1]: Iqbal, Asifa, and Vania Ceccato. "Is CPTED useful to guide the inventory of safety in parks? A study case in Stockholm, Sweden." _International criminal justice review_ 26, no. 2 (2016): 150-168.
 [^2]: Jacobs, Jane. "Jane jacobs." _The Death and Life of Great American Cities_ 21, no. 1 (1961): 13-25.
 [^3]: Gardner, Carol Brooks. _Passing by: Gender and public harassment_. Univ of California Press, 1995.
 [^4]: “Documenting Street Harassment in Bengaluru.” Safe Yelli in Bengaluru? Accessed December 5, 2022. https://safeyelli.in/. The SafeYelli project is led by me and has informed all of my contextual knowledge on safety that I might imply
 [^5]: Safecity. https://www.safecity.in/.
 [^6]: “Safetipin, Creating Safe Public Spaces for Women.” Safetipin. Accessed December 5, 2022. https://safetipin.com/.
 [^7]: Paul, Tanusree. "Public Spaces and Everyday Lives: Gendered Encounters in the Metro City of Kolkata." In _Doing Gender, Doing Geography_, pp. 264-283. Routledge India, 2012.
 [^8]: Anwar, Sajjad. “Mapping Public Transit in Bangalore.” Mapbox Blog. MapBox, June 29, 2017. https://blog.mapbox.com/mapping-public-transit-in-bangalore-32cb80d18e02.
 [^9]: Stadler, Timo, Simon Hofmeister, and Jan Dunnweber. “Hawaii International Conference on System Sciences.” In _A Method for the Optimized Placement of Bus Stops Based on Voronoi Diagram_, n.d. https://scholarspace.manoa.hawaii.edu/server/api/core/bitstreams/0fb14ccf-a5dd-4660-8b56-ceab7f9c1a2b/content.
[^10]: “Home - Bureau of Indian Standards.” Accessed December 5, 2022. https://www.bis.gov.in/.
