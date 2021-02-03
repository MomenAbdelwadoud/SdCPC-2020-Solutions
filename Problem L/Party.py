import math
def party(x_home,y_home,x_event,y_event,st_event,st_prep,d_event,d_prep):
    dist = math.sqrt((x_home-x_event)**2 + (y_home-y_event)**2)
    car_time = dist / s
    parents_time = math.ceil(car_time + st_event + d_event)
    prep_time = st_prep + d_prep
    if prep_time > parents_time:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    with open('party.in') as f:
        _ = list(map(int,f.readline().split()))
        x_home = _[0]
        y_home = _[1]
        _ = list(map(int,f.readline().split()))
        x_event = _[0]
        y_event = _[1]
        s = int(f.readline())
        _ = list(map(int,f.readline().split()))
        st_event = _[0]
        st_prep = _[1]
        _ = list(map(int,f.readline().split()))
        d_event = _[0]
        d_prep = _[1]
        print(party(x_home,y_home,x_event,y_event,st_event,st_prep,d_event,d_prep))