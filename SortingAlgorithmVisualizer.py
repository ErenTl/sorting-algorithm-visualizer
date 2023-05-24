import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import matplotlib
# matplotlib.use('Qt5Agg')

COLOR_COMPARISON = 'red'  # Karşılaştırma yapılan elemanlar için renk
COLOR_SWAP = 'blue'  # Değerlerin yerlerini değiştirirken kullanılan renk
COLOR_SORTED = 'green'  # Sıralanmış elemanlar için renk
COLOR_UNSORTED = 'gray'  # Sıralanmamış elemanlar için renk
comparisonCount = 0
pause = False

# Tkinter uygulamasını oluşturma
app = tk.Tk()
app.title("Sıralama Algoritması ve Grafik Görselleştirme")

# Değişkenler
data = []
algorithm = tk.StringVar()
algorithm.set("Seçme Sıralaması")
graph_type = tk.StringVar()
graph_type.set("Sütun (Bar) Grafiği")
sorting = False

# def start_loop():
#     global pause
#     for i in range(10):
#         print(i)
#         # İşlemleriniz burada yer alır
#         app.update()  # Arayüzü güncelle
#         if not pause:
#             break

def pauseSorting ():
    global pause
    pause = True
    print("pause")

def continueSorting ():
    global pause
    pause = False

# Sıralama algoritmaları
# def selection_sort():
#     print("selection sort")
#     global data
#     print(data)
#     n = len(data)
#     plt.ion()

#     for i in range(n):
#         # time.sleep(2)
#         min_idx = i
#         for j in range(i+1, n):
#             if data[j] < data[min_idx]:
#                 min_idx = j
#         data[i], data[min_idx] = data[min_idx], data[i]
#         create_graph()
#         mypause(5)
#     plt.ioff()
#     print("end")

def get_speed():
    global speed_slider
    new_speed = (speed_slider.get()-11)*-0.01
    return new_speed

def selection_sort():
    print("Selection sort")
    global data
    n = len(data)
    plt.ion()

    for i in range(n):
        min_index = i

        create_graph()
        color_array = [COLOR_UNSORTED] * n
        color_array[:i] = [COLOR_SORTED] * i
        create_graph_carray(n, data, color_array)
        mypause(get_speed())
        plt.clf()

        for j in range(i + 1, n):
            create_graph()
            color_array = [COLOR_UNSORTED] * n
            color_array[:i] = [COLOR_SORTED] * i
            color_array[i] = COLOR_SWAP
            color_array[j] = COLOR_COMPARISON
            global comparisonCount
            comparisonCount += 1
            create_graph_carray(n, data, color_array)
            mypause(get_speed())
            while pause:
                app.update()
            plt.clf()

            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

        create_graph()
        color_array = [COLOR_UNSORTED] * n
        color_array[:i+1] = [COLOR_SORTED] * (i+1)
        create_graph_carray(n, data, color_array)
        mypause(get_speed())
        plt.clf()

    plt.ioff()
    color_array = [COLOR_SORTED] * n
    create_graph_carray(n, data, color_array)
    print("end")


def merge_sort_with_color():
    print("Merge sort")
    global data
    n = len(data)
    plt.ion()
    
    result = merge_sort_helper(data)
    
    for i in range(n):
        create_graph()
        color_array = [COLOR_UNSORTED] * n
        color_array[:i+1] = [COLOR_SORTED] * (i+1)
        create_graph_carray(n, result, color_array)
        mypause(get_speed())
        plt.clf()
        
        print(result)

    plt.ioff()
    color_array = [COLOR_SORTED] * n
    create_graph_carray(n, result, color_array)
    print("end")

def merge_sort_helper(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort_helper(left_half)
    right_half = merge_sort_helper(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        create_graph()
        color_array = [COLOR_UNSORTED] * len(left) + [COLOR_COMPARISON] * (i + 1)
        color_array += [COLOR_UNSORTED] * len(right) + [COLOR_COMPARISON] * (j + 1)
        print("left: ", len(left))
        print("right: ", right)
        print("color array: ", color_array)
        create_graph_carray(len(left) + len(right), left + right, color_array)
        mypause(get_speed())        
        plt.clf()
        
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    while len(result) < len(left) + len(right):
        result.append(right[j])
        j += 1
    
    create_graph()
    color_array = [COLOR_SORTED] * len(result)
    create_graph_carray(len(left) + len(right), result, color_array)
    mypause(get_speed())        
    plt.clf()
    
    return result


def quicksort_with_color():
    print("Quicksort")
    global data
    n = len(data)
    plt.ion()
    
    quicksort_helper(data, 0, n-1)
    
    color_array = [COLOR_SORTED] * n
    # plt.bar(range(n), data, color=color_array)
    create_graph_carray(n, data, color_array)

    # plt.show()
    plt.ioff()
    print("end")

def quicksort_helper(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_helper(arr, low, pi-1)
        quicksort_helper(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    global data
    
    for j in range(low, high):
        create_graph()
        color_array = [COLOR_UNSORTED] * len(arr)
        color_array[j] = COLOR_COMPARISON
        color_array[high] = COLOR_COMPARISON
        create_graph_carray(len(arr), data, color_array)
        mypause(get_speed())        
        plt.clf()
        
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            create_graph()
            color_array = [COLOR_UNSORTED] * len(arr)
            color_array[i] = COLOR_SWAP
            color_array[j] = COLOR_SWAP
            create_graph_carray(len(arr), data, color_array)
            mypause(get_speed())        
            plt.clf()
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    create_graph()
    color_array = [COLOR_UNSORTED] * len(arr)
    color_array[i+1] = COLOR_SWAP
    color_array[high] = COLOR_SWAP
    create_graph_carray(len(arr), data, color_array)
    mypause(get_speed())        
    plt.clf()
    
    return i+1



# def insertion_sort():
#     print("Insertion sort")
#     global data
#     print(data)
#     n = len(data)
#     plt.ion()

#     for i in range(1, n):
#         key = data[i]
#         j = i - 1

#         while j >= 0 and data[j] > key:
#             # Karşılaştırma yapılacak elemanları renklendirme
#             create_graph()
#             color_array = [COLOR_UNSORTED] * n
#             color_array[j] = COLOR_COMPARISON
#             color_array[j + 1] = COLOR_COMPARISON
#             plt.bar(range(n), data, color=color_array)
#             mypause(1)
#             plt.clf()  # Grafik temizleme

#             data[j + 1] = data[j]
#             j -= 1

#         data[j + 1] = key

#         # Yer değiştirilen değeri renklendirme
#         create_graph()
#         color_array = [COLOR_UNSORTED] * n
#         color_array[j + 1] = COLOR_SWAP
#         plt.bar(range(n), data, color=color_array)
#         mypause(1)
#         plt.clf()  # Grafik temizleme

#         # Sıralanmış ve sıralanmamış elemanları renklendirme
#         create_graph()
#         color_array = [COLOR_SORTED] * (i + 1) + [COLOR_UNSORTED] * (n - i - 1)
#         plt.bar(range(n), data, color=color_array)
#         mypause(1)
#         plt.clf()  # Grafik temizleme

#     plt.ioff()
#     print("end")

def create_graph_carray(n, data, color_array):
    if len(color_array) != len(data):
        color_array = color_array[:len(data)]  # Renk dizisini veri dizisiyle aynı boyuta getir
    # global data
    print("create graph carray")
    plt.cla()
    if graph_type.get() == "Dağılım (Scatter) Grafiği":
        plt.scatter(range(n), data, color=color_array)
        print("scatter")
    elif graph_type.get() == "Sütun (Bar) Grafiği":
        plt.bar(range(n), data, color=color_array)
        print("bar")
    elif graph_type.get() == "Kök (Stem) Grafiği":
        for i in range(n):
            plt.stem([i], [data[i]], linefmt=color_array[i], markerfmt='o', basefmt=' ')
        print("stem")
    global comparisonCount
    # plt.title(algorithm.get() + " - " + "Karşılaştırma Sayısı: " + comparisonCount.__str__() )
    plt.xlabel("Index")
    plt.ylabel("Value")

# Grafik oluşturma
def create_graph():
    global data
    print("create graph")
    # print(data)
    plt.cla()
    if graph_type.get() == "Dağılım (Scatter) Grafiği":
        plt.scatter(range(len(data)), data, color='b')
        print("scatter")
    elif graph_type.get() == "Sütun (Bar) Grafiği":
        plt.bar(range(len(data)), data, color='b')
        print("bar")
    elif graph_type.get() == "Kök (Stem) Grafiği":
        plt.stem(range(len(data)), data)
        print("stem")
    global comparisonCount
    plt.title(algorithm.get() + " - " + "Karşılaştırma Sayısı: " + comparisonCount.__str__() )
    plt.xlabel("Index")
    plt.ylabel("Value")



def mypause(interval):
    backend = plt.rcParams['backend']
    if backend in matplotlib.rcsetup.interactive_bk:
        figManager = matplotlib._pylab_helpers.Gcf.get_active()
        if figManager is not None:
            canvas = figManager.canvas
            if canvas.figure.stale:
                canvas.draw()
            canvas.start_event_loop(interval)
            return


# Sıralama animasyonu
def sort_animation():
    global sorting
    global comparisonCount
    sorting = True
    comparisonCount = 0
    if algorithm.get() == "Seçme Sıralaması":
        selection_sort()
    elif algorithm.get() == "Kabarcık Sıralaması":
        bubble_sort()
    elif algorithm.get() == "Ekleme Sıralaması":
        insertion_sort()
    elif algorithm.get() == "Birleştirme Sıralaması":
        merge_sort_with_color()
    elif algorithm.get() == "Hızlı Sıralama":
        quicksort_with_color()
    sorting = False

# Animasyon güncelleme
def update_animation(frame):
    global sorting
    if not sorting:
        return
    create_graph()
    sort_animation()

# Başlat/Duraklat butonu işlevi
def start_pause_animation():
    global sorting
    if not sorting:
        sorting = True
        sort_animation()
    else:
        sorting = False

# Yeni liste oluşturma
def generate_list():
    global data
    size = int(entry_size.get())
    data = random.sample(range(1, 101), size)
    create_graph()

# Arayüz bileşenlerinin oluşturulması
frame_left = tk.Frame(app)
frame_left.pack(side="left", padx=10, pady=10)

label_size = tk.Label(frame_left, text="Boyut:")
label_size.pack()
entry_size = tk.Entry(frame_left)
entry_size.pack()

button_generate = tk.Button(frame_left, text="Oluştur", command=generate_list)
button_generate.pack(pady=5)

label_algorithm = tk.Label(frame_left, text="Sıralama Algoritması:")
label_algorithm.pack()
dropdown_algorithm = tk.OptionMenu(frame_left, algorithm, "Seçme Sıralaması", "Kabarcık Sıralaması", "Ekleme Sıralaması", "Birleştirme Sıralaması", "Hızlı Sıralama")
dropdown_algorithm.pack(pady=5)

label_graph_type = tk.Label(frame_left, text="Grafik Türü:")
label_graph_type.pack()
dropdown_graph_type = tk.OptionMenu(frame_left, graph_type, "Sütun (Bar) Grafiği", "Dağılım (Scatter) Grafiği", "Kök (Stem) Grafiği")
dropdown_graph_type.pack(pady=5)

speed_label = ttk.Label(frame_left, text="Hız:")
speed_label.pack(pady=5)
speed_slider = ttk.Scale(frame_left, from_=1, to=10, orient=tk.HORIZONTAL)
speed_slider.pack(pady=5)

button_start_pause = tk.Button(frame_left, text="Başlat", command=start_pause_animation)
button_start_pause.pack(pady=5)

button_pause = tk.Button(frame_left, text="Duraklat", command=pauseSorting)
button_pause.pack(pady=5)

button_continue = tk.Button(frame_left, text="Devam", command=continueSorting)
button_continue.pack(pady=5)




# Animasyon için Matplotlib figürünün oluşturulması
figure = plt.figure()
chart = figure.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(figure, update_animation, interval=100)

# Grafik gösterimi
frame_right = tk.Frame(app)
frame_right.pack(side="right", padx=10, pady=10)
canvas = FigureCanvasTkAgg(figure, master=frame_right)
canvas.draw()
canvas.get_tk_widget().pack()

# Uygulamanın başlatılması
app.mainloop()
