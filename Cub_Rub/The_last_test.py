from ursina import *
import time
import cv2
import numpy as np
from collections import Counter
import kociemba

cap = cv2.VideoCapture(0)

CALIBRATION_ORDER = [
    'white',
    'red',
    'green',
    'yellow',
    'orange',
    'blue'
]

def get_color_name(bgr, references):
    min_distance = float('inf')
    closest_color = 'unknown'
    for color_name, ref_color in references.items():
        distance = np.sqrt(np.sum((np.array(bgr) - np.array(ref_color))**2))
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name
    return closest_color

def calibrate_colors():
    references = {}
    print("=== НАЧИНАЕМ КАЛИБРОВКУ ===")
    print("Наводите центр кубика с нужным цветом в квадрат и нажимайте пробел\n")
    
    for color in CALIBRATION_ORDER:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue
                
            frame = cv2.flip(frame, 1)
            h, w = frame.shape[:2]
            x_center = w // 2
            y_center = h // 2
            
     
            cv2.rectangle(frame, (x_center-40, y_center-40), 
                          (x_center+40, y_center+40), (0, 255, 0), 2)
            cv2.putText(frame, f"Calibrate {color}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            cv2.imshow("Calibration", frame)
            key = cv2.waitKey(1) & 0xFF
            
            if key == 27:
                cap.release()
                cv2.destroyAllWindows()
                exit()
            elif key == 32:
                b, g, r = frame[y_center, x_center]
                references[color] = [int(b), int(g), int(r)]
                print(f"{color} calibrated: {references[color]}")
                break
                
    cv2.destroyWindow("Calibration")
    return references

def scan_faces(references):
    OUR_count = 0
    all_faces = []
    
    while OUR_count < 6:
        ret, frame = cap.read()
        if not ret:
            continue
            
        frame = cv2.flip(frame, 1)
        s = 100
        spis = []
        kort = [-1, 0, 1]
        kort2 = [1, 0, -1]
        h, w, _ = frame.shape

        for y_ in kort:
            for x_ in kort2:
                x_center = w // 2 + x_ * s
                y_center = h // 2 + y_ * s
                cv2.rectangle(frame, (x_center-40, y_center-40),
                              (x_center+40, y_center+40), (0,255,0), 2)
                b, g, r = frame[y_center, x_center]
                color_name = get_color_name([b,g,r], references)
                spis.append(color_name)

        cv2.imshow("Scan Faces", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == 27:
            break
        elif key == 32:
            all_faces.append(spis.copy())
            print(f"Грань {OUR_count+1} сохранена")
            OUR_count += 1
            
    return all_faces


references = calibrate_colors()
all_faces = scan_faces(references)

all_colors = [color for face in all_faces for color in face] 
color_counts = Counter(all_colors) 

valid = True

for color in CALIBRATION_ORDER:
    count = color_counts.get(color, 0)
    if count != 9:
        print(f"Ошибка: цвет '{color}' встречается {count} раз вместо 9.")
        valid = False


if 'unknown' in color_counts:
    print(f"Ошибка: обнаружено {color_counts['unknown']} неизвестных цветов.")
    valid = False

if not valid:
    print("\nПроверка не пройдена. Убедитесь, что все цвета распознаны верно и повторите сканирование.")
    cap.release()
    cv2.destroyAllWindows()
    exit()


print("\nРезультаты сканирования:")
for i, face in enumerate(all_faces, 1):
    print(f"\nГрань {i}:")
    for row in range(3):
        print(" | ".join(f"{color:<8}" for color in face[row*3:(row+1)*3]))
print(all_faces)
koceimba = ''
for face in all_faces:
    for i in face:
        koceimba += i[0]
stroka = koceimba
koceimba = koceimba.upper()



koceimba = koceimba.replace('W','U')
koceimba = koceimba.replace('G','F')
koceimba = koceimba.replace('Y','D')
koceimba = koceimba.replace('O','L')

print(koceimba)
print("========")
print(stroka)
print("========")


cap.release()

cv2.destroyAllWindows()

# stroka = stroka.replace('y','w')
# stroka = stroka.replace('b','g')
# stroka = stroka.replace('r','o')


contetnt = str(stroka)
for i in range(9, 18):
    if contetnt[i] == 'w':
        contetnt = contetnt[:i] + "y" + contetnt[i+1:]
    elif contetnt[i] == 'r':
        contetnt = contetnt[:i] + "o" + contetnt[i+1:]
    elif contetnt[i] == 'g':
        contetnt = contetnt[:i] + "b" + contetnt[i+1:]
    elif contetnt[i] == 'y':
        contetnt = contetnt[:i] + "w" + contetnt[i+1:]
    elif contetnt[i] == 'o':
        contetnt = contetnt[:i] + "r" + contetnt[i+1:]
    elif contetnt[i] == 'b':
        contetnt = contetnt[:i] + "g" + contetnt[i+1:]
    
for j in range(27, 36):
    if contetnt[j] == 'w':
        contetnt = contetnt[:j] + "y" + contetnt[j+1:]
    elif contetnt[j] == 'r':
        contetnt = contetnt[:j] + "o" + contetnt[j+1:]
    elif contetnt[j] == 'g':
        contetnt = contetnt[:j] + "b" + contetnt[j+1:]
    elif contetnt[j] == 'y':
        contetnt = contetnt[:j] + "w" + contetnt[j+1:]
    elif contetnt[j] == 'o':
        contetnt = contetnt[:j] + "r" + contetnt[j+1:]
    elif contetnt[j] == 'b':
        contetnt = contetnt[:j] + "g" + contetnt[j+1:]

for h in range(45, 54):
    if contetnt[h] == 'w':
        contetnt = contetnt[:h] + "y" + contetnt[h+1:]
    elif contetnt[h] == 'r':
        contetnt = contetnt[:h] + "o" + contetnt[h+1:]
    elif contetnt[h] == 'g':
        contetnt = contetnt[:h] + "b" + contetnt[h+1:]
    elif contetnt[h] == 'y':
        contetnt = contetnt[:h] + "w" + contetnt[h+1:]
    elif contetnt[h] == 'o':
        contetnt = contetnt[:h] + "r" + contetnt[h+1:]
    elif contetnt[h] == 'b':
        contetnt = contetnt[:h] + "g" + contetnt[h+1:]

file_name="Bound_Rubiks.txt"
with open (f"{file_name}",'w') as file_object:
    file_object.write(contetnt)
print('=======================')
print('=======================')
print('=======================')
with open (f"{file_name}",'r') as file_object:
    contetnt = file_object.readline()
    print(contetnt)
print('=======================')
print('=======================')
print('=======================')



# contetnt = "goygwbwrboygoowwgrogwggwgyrwgbowobygwwbooowyoowobggwrr"
def have_two_or_more_matches(a: list, b: list) -> bool:
    matches = sum(1 for x, y in zip(a, b) if x == y)
    return matches >= 2




dict = {
    "0": [contetnt[38],contetnt[6],contetnt[18]],
    "1": [contetnt[37],contetnt[3],None],
    "2": [contetnt[36],contetnt[0],contetnt[47]],
    "3": [None,contetnt[7],contetnt[19]],
    "4": [None,contetnt[4],None],
    "5": [None,contetnt[1],contetnt[46]],
    "6": [contetnt[9],contetnt[8],contetnt[20]],
    "7": [contetnt[10],contetnt[5],None],
    "8": [contetnt[11],contetnt[2],contetnt[45]],

    "9": [contetnt[41],None,contetnt[21]],
    "10": [contetnt[40],None,None],
    "11": [contetnt[39],None,contetnt[50]],
    "12": [None,None,contetnt[22]],
    "13": [None,None,None],
    "14": [None,None,contetnt[49]],
    "15": [contetnt[12],None,contetnt[23]],
    "16": [contetnt[13],None,None],
    "17": [contetnt[14],None,contetnt[48]],
    
    "18": [contetnt[44],contetnt[27],contetnt[24]],
    "19": [contetnt[43],contetnt[30],None],
    "20": [contetnt[42],contetnt[33],contetnt[53]],
    "21": [None,contetnt[28],contetnt[25]],
    "22": [None,contetnt[31],None],
    "23": [None,contetnt[34],contetnt[52]],
    "24": [contetnt[15],contetnt[29],contetnt[26]],
    "25": [contetnt[16],contetnt[32],None],
    "26": [contetnt[17],contetnt[35],contetnt[51]],
}

dict_rotation_1 = [["o","w","g"],["g","w","r"],["r","w","b"],["b","w","o"],
                 ["w","r","g"],["g","r","y"],["y","r","b"],["b","r","w"],
                 ["o","g","y"],["y","g","r"],["r","g","w"],["w","g","o"],
                 ["o","y","b"],["b","y","r"],["r","y","g"],["g","y","o"],
                 ["y","o","g"],["g","o","w"],["w","o","b"],["b","o","y"],
                 ["o","b","w"],["w","b","r"],["r","b","y"],["y","b","o"]]

dict_rotation_2 = [(0,0,0),(0,90,0),(0,180,0),(0,270,0),
                   (0,0,270),(0,90,270),(0,180,270),(0,270,270),
                   (90,0,0),(90,90,0),(90,180,0),(90,270,0),
                   (180,0,0),(180,90,0),(180,180,0),(180,270,0),
                   (0,0,90),(0,90,90),(0,180,90),(0,270,90),
                   (270,0,0),(270,90,0),(270,180,0),(270,270,0)]

big_rotation = []
for dict_i in range(27):
    fast_per = dict[str(dict_i)]
    for dict_rotation_1_i in range(24):
        if have_two_or_more_matches(fast_per,dict_rotation_1[dict_rotation_1_i]):
            big_rotation.append(dict_rotation_2[dict_rotation_1_i])
print(len(big_rotation))
BIG_rotation = (
    big_rotation[0], big_rotation[3], big_rotation[5], big_rotation[1],
    (0, 0, 0),
    big_rotation[6], big_rotation[2], big_rotation[4], big_rotation[7], big_rotation[8],
    (0, 0, 0),
    big_rotation[10],
    (0, 0, 0), (0, 0, 0), (0, 0, 0),
    big_rotation[9],
    (0, 0, 0),
    big_rotation[11], big_rotation[12], big_rotation[15], big_rotation[17], big_rotation[13],
    (0, 0, 0),
    big_rotation[18], big_rotation[14], big_rotation[16], big_rotation[19]
)



print(len(BIG_rotation))

print(len(big_rotation))
app = Ursina()
massiv = []
Sky(texture='sky.png')


# создаем кубики 3x3x3
count = 0
for y in [1, 0, -1]:
    for z in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            x_r, y_r, z_r = BIG_rotation[count]
            cube = Entity(
                model='cube.obj',
                position=Vec3(x, y, z),
                texture='texture.png',
                scale=0.5,
                rotation = (x_r, y_r, z_r)
            )
            count += 1
            massiv.append(cube)

dictionary = {key: [] for key in massiv}

dictionary[massiv[0]] = ['orange','white','green']
dictionary[massiv[1]] = ['orange','white','None']
dictionary[massiv[2]] = ['orange','white','blue']
dictionary[massiv[3]] = ['None','white','green']
dictionary[massiv[4]] = ['None','white','None']
dictionary[massiv[5]] = ['None','white','blue']
dictionary[massiv[6]] = ['red','white','green']
dictionary[massiv[7]] = ['red','white','None']
dictionary[massiv[8]] = ['red','white','blue']

dictionary[massiv[9]] = ['orange','None','green']
dictionary[massiv[10]] = ['orange','None','None']
dictionary[massiv[11]] = ['orange','None','blue']
dictionary[massiv[12]] = ['None','None','green']
dictionary[massiv[13]] = ['None','None','None']
dictionary[massiv[14]] = ['None','None','blue']
dictionary[massiv[15]] = ['red','None','green']
dictionary[massiv[16]] = ['red','None','None']
dictionary[massiv[17]] = ['red','None','blue']

dictionary[massiv[18]] = ['orange','yellow','green']
dictionary[massiv[19]] = ['orange','yellow','None']
dictionary[massiv[20]] = ['orange','yellow','blue']
dictionary[massiv[21]] = ['None','yellow','green']
dictionary[massiv[22]] = ['None','yellow','None']
dictionary[massiv[23]] = ['None','yellow','blue']
dictionary[massiv[24]] = ['red','yellow','green']
dictionary[massiv[25]] = ['red','yellow','None']
dictionary[massiv[26]] = ['red','yellow','blue']


def rotate_position(pos, axis, clockwise=True):
    x, y, z = pos
    if axis == 'y':
        return Vec3(-z, y, x) if clockwise else Vec3(z, y, -x)
    elif axis == 'x':
        return Vec3(x, -z, y) if clockwise else Vec3(x, z, -y)
    elif axis == 'z':
        return Vec3(-y, x, z) if clockwise else Vec3(y, -x, z)


def rotate_layer(condition, axis, clockwise):
    layer = [cube for cube in massiv if condition(cube)]


    center = Vec3(0, 0, 0)
    for cube in layer:
        center += cube.position
    center /= len(layer)

    pivot = Entity(position=center)

    for cube in layer:
        cube.world_parent = pivot

    angle = 90 if clockwise else -90
    duration = 0.5 

    if axis == 'x':
        pivot.animate_rotation_x(pivot.rotation_x + angle, duration=duration)
    elif axis == 'y':
        pivot.animate_rotation_y(pivot.rotation_y + angle, duration=duration)
    elif axis == 'z':
        pivot.animate_rotation_z(pivot.rotation_z + angle, duration=duration)

    def finalize():
        for cube in layer:
            cube.world_parent = scene
            cube.position = Vec3(round(cube.x), round(cube.y), round(cube.z))
            cube.rotation = Vec3(
                round(cube.rotation_x / 90) * 90,
                round(cube.rotation_y / 90) * 90,
                round(cube.rotation_z / 90) * 90
            )
        destroy(pivot)

    invoke(finalize, delay=duration + 0.01)


def rotate_upper_bound_in_left(): 
    rotate_layer(lambda c: round(c.y) == 1, axis='y', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.y) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [z, y, x]
def rotate_upper_bound_in_right(): 
    rotate_layer(lambda c: round(c.y) == 1, axis='y', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.y) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [z, y, x]
def rotate_down_bound_in_left(): 
    rotate_layer(lambda c: round(c.y) == -1, axis='y', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.y) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [z, y, x]
def rotate_down_bound_in_right(): 
    rotate_layer(lambda c: round(c.y) == -1, axis='y', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.y) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [z, y, x]

def rotate_left_bound_in_up(): 
    rotate_layer(lambda c: round(c.x) == -1, axis='x', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.x) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [x, z, y]
def rotate_left_bound_in_down(): 
    rotate_layer(lambda c: round(c.x) == -1, axis='x', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.x) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [x, z, y]
def rotate_right_bound_in_up(): 
    rotate_layer(lambda c: round(c.x) == 1, axis='x', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.x) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [x, z, y]
def rotate_right_bound_in_down(): 
    rotate_layer(lambda c: round(c.x) == 1, axis='x', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.x) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [x, z, y]

def rotate_front_bound_in_left(): 
    rotate_layer(lambda c: round(c.z) == -1, axis='z', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.z) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [y, x, z]
def rotate_front_bound_in_right(): 
    rotate_layer(lambda c: round(c.z) == -1, axis='z', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.z) == -1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [y, x, z]
def rotate_back_bound_in_left(): 
    rotate_layer(lambda c: round(c.z) == 1, axis='z', clockwise=True)
    layer = [cube for cube in massiv if round(cube.position.z) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [y, x, z]
def rotate_back_bound_in_right(): 
    rotate_layer(lambda c: round(c.z) == 1, axis='z', clockwise=False)
    layer = [cube for cube in massiv if round(cube.position.z) == 1]
    for cube in layer:
        x, y, z = dictionary[cube]
        dictionary[cube] = [y, x, z]

def cube_assembly(koceimba):
    
    time_offset = 0
    t = 1.1
    for move in sol_list:
        if move == "U":
            invoke(rotate_upper_bound_in_left, delay=time_offset)
            time_offset += t
        elif move == "U'":
            invoke(rotate_upper_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "U2":
            invoke(rotate_upper_bound_in_left, delay=time_offset)
            time_offset += t
            invoke(rotate_upper_bound_in_left, delay=time_offset)
            time_offset += t
        elif move == "R":
            invoke(rotate_right_bound_in_up, delay=time_offset)
            time_offset += t
        elif move == "R'":
            invoke(rotate_right_bound_in_down, delay=time_offset)
            time_offset += t
        elif move == "R2":
            invoke(rotate_right_bound_in_up, delay=time_offset)
            time_offset += t
            invoke(rotate_right_bound_in_up, delay=time_offset)
            time_offset += t
        elif move == "F'":
            invoke(rotate_front_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "F":
            invoke(rotate_front_bound_in_left, delay=time_offset)
            time_offset += t
        elif move == "F2":
            invoke(rotate_front_bound_in_right, delay=time_offset)
            time_offset += t
            invoke(rotate_front_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "D":
            invoke(rotate_down_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "D'":
            invoke(rotate_down_bound_in_left, delay=time_offset)
            time_offset += t
        elif move == "D2":
            invoke(rotate_down_bound_in_right, delay=time_offset)
            time_offset += t
            invoke(rotate_down_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "L":
            invoke(rotate_left_bound_in_down, delay=time_offset)
            time_offset += t
        elif move == "L'":
            invoke(rotate_left_bound_in_up, delay=time_offset)
            time_offset += t
        elif move == "L2":
            invoke(rotate_left_bound_in_down, delay=time_offset)
            time_offset += t
            invoke(rotate_left_bound_in_down, delay=time_offset)
            time_offset += t
        elif move == "B":
            invoke(rotate_back_bound_in_right, delay=time_offset)
            time_offset += t
        elif move == "B'":
            invoke(rotate_back_bound_in_left, delay=time_offset)
            time_offset += t
        elif move == "B2":
            invoke(rotate_back_bound_in_left, delay=time_offset)
            time_offset += t
            invoke(rotate_back_bound_in_left, delay=time_offset)
            time_offset += t



current_layer = None
date = time.time()
sol = kociemba.solve(koceimba)
print(time.time() - date)
sol_list = sol.split()
print(sol_list)


def input(key):
    global current_layer


    if key == '1': current_layer = 'upper'
    elif key == '2': current_layer = 'down'
    elif key == '3': current_layer = 'left'
    elif key == '4': current_layer = 'right'
    elif key == '5': current_layer = 'front'
    elif key == '6': current_layer = 'back'

    # стрелки — поворот выбранной грани
    elif key == 'left arrow':
        if current_layer == 'upper': rotate_upper_bound_in_left()
        elif current_layer == 'down': rotate_down_bound_in_left()
        elif current_layer == 'front': rotate_front_bound_in_left()
        elif current_layer == 'back': rotate_back_bound_in_left()
    elif key == 'right arrow':
        if current_layer == 'upper': rotate_upper_bound_in_right()
        elif current_layer == 'down': rotate_down_bound_in_right()
        elif current_layer == 'front': rotate_front_bound_in_right()
        elif current_layer == 'back': rotate_back_bound_in_right()
    elif key == 'up arrow':
        if current_layer == 'left': rotate_left_bound_in_up()
        elif current_layer == 'right': rotate_right_bound_in_up()
    elif key == 'down arrow':
        if current_layer == 'left': rotate_left_bound_in_down()
        elif current_layer == 'right': rotate_right_bound_in_down()

    elif key == "7":
        cube_assembly(sol_list)

# камера
EditorCamera(rotation=(20, 20, 0), distance=20)

app.run()


print("========")
print(stroka)
print("========")
