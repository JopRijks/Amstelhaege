def location_checker(house, neighbourhood):
    # vertical wall check - horizontal wall check - inside check
    mindistance= []
    vert = list(range(house.y0, house.y1))
    horz = list(range(house.x0, house.x1))
    for i in neighbourhood:
        if i.name == "WATER":
            horzWater = list(range(i.x0, i.x1))
            vertWater = list(range(i.y0, i.y1))
            if (house.x0 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y0 in vertWater):
                return False
            elif (house.x0 in horzWater and house.y1 in vertWater):
                return False
            elif (house.x1 in horzWater and house.y1 in vertWater):
                return False     
        else:
            if (house.x0 -2 <= i.x0 and house.x1+2 >= i.x0) or (house.x0-2 <= i.x1 and house.x1+2 >= i.x1):
                if (house.y0-2 <= i.y0 and house.y1+2 >= i.y0) or (house.y0-2 <= i.y1 and house.y1+2 >= i.y1):
                    return False
            if i.y0 in vert or i.y1 in vert:
                min_distance = min([abs(house.x0-i.x1),abs(house.x1-i.x0),abs(house.x1-i.x1),abs(house.x0-i.x0)])
                mindistance.append(min_distance)          
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
                elif min_distance < i.shortest_distance :
                    #print(i.shortest_distance,min_distance)
                    i.shortest_distance = min_distance
            elif i.x0 in horz or i.x1 in horz:
                min_distance = min([abs(house.y0-i.y1),abs(house.y1-i.y0),abs(house.y1-i.y1),abs(house.y0-i.y0)])
                mindistance.append(min_distance)           
                if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                    return False
                elif min_distance < i.shortest_distance :
                    #print(i.shortest_distance,min_distance)
                    i.shortest_distance = min_distance
            elif house.y1 < i.y0:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y1,i.x0,i.y0)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y1,i.x1,i.y0)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance                                                    
            elif house.y0 > i.y1:
                if house.x1 < i.x0:
                    min_distance = distanceCalc(house.x1,house.y0,i.x0,i.y1)
                    mindistance.append(min_distance) 
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden                    
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance 
                elif house.x0 > i.x1:
                    min_distance = distanceCalc(house.x0,house.y0,i.x1,i.y1)
                    mindistance.append(min_distance)  
                    if house.free_area > abs(min_distance) or i.free_area > abs(min_distance): #absolute omdat anders negatieve afstanden
                        return False
                    elif min_distance < i.shortest_distance :
                        #print(i.shortest_distance,min_distance)
                        i.shortest_distance = min_distance
    if len(mindistance) > 0:
        #print(min(mindistance))
        house.shortest_distance = min(mindistance)
    return True

def distanceCalc(x0,y0,x1,y1):
    return abs(((x1-x0)**2+(y1-y0)**2)**0.5)