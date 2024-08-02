travel=[{
    "country":"france",
    "visitss":12,
    "cities":["paris","lille"]
},
{
    "country":"france",
    "visitss":5,
    "cities":["paris","lille"]

}
]
def country(name,list):
    new_country={}
    new_country["country"]=name
    
    new_country["cities"]=list
    travel.append(new_country)
country(country,list)
print(f"i have been to {travel[2]['country']} times.")
print(f"my fav city was {travel[2]['cities'][0]}")