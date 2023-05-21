import tkinter as tk
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
def selection_sort():
    print("selection sort")
    global data
    print(data)
    n = len(data)
    plt.ion()

    for i in range(n):
        # time.sleep(2)
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        create_graph()
        mypause(5)
    plt.ioff()
    print("end")

def bubble_sort():
    print("Bubble sort")
    global data
    # print(data)
    n = len(data)
    plt.ion()
    greenColors = 0

    for i in range(n - 1):
        for j in range(n - i - 1):
            # Karşılaştırma yapılacak elemanları renklendirme
            create_graph()
            
            print("greenColors",greenColors)
            if greenColors != 0:
                color_array = ([COLOR_UNSORTED] * (n -greenColors)) +( [COLOR_SORTED] * (greenColors))
            else:
                color_array = [COLOR_UNSORTED] * n
            # print(color_array )
            color_array[j] = COLOR_COMPARISON
            color_array[j + 1] = COLOR_COMPARISON
            global comparisonCount
            comparisonCount += 1
            plt.bar(range(n), data, color=color_array)
            mypause(0.0005)
            while pause:
                app.update()
            plt.clf()  # Grafik temizleme

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                # Yer değiştirilen değerleri renklendirme
                create_graph()
                color_array[j] = COLOR_SWAP
                color_array[j + 1] = COLOR_SWAP
                plt.bar(range(n), data, color=color_array)
                mypause(0.0005)
                plt.clf()  # Grafik temizleme

        # Sıralanmış ve sıralanmamış elemanları renklendirme
        create_graph()
        color_array = [COLOR_UNSORTED] * (n - i - 1) + [COLOR_SORTED] * (i + 1)
        greenColors = i+1
        plt.bar(range(n), data, color=color_array)
        mypause(0.0005)
        # plt.clf()  # Grafik temizleme

    plt.ioff()
    color_array = [COLOR_SORTED] * n
    plt.bar(range(n), data, color=color_array)
    print("end")

# def bubble_sort():
#     global data
#     n = len(data)
#     plt.ion()
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]
#                 create_graph()
#                 mypause(1)
#     plt.ioff()
#     print("end")


def insertion_sort():
    print("Insertion sort")
    global data
    print(data)
    n = len(data)
    plt.ion()

    for i in range(1, n):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            # Karşılaştırma yapılacak elemanları renklendirme
            create_graph()
            color_array = [COLOR_UNSORTED] * n
            color_array[j] = COLOR_COMPARISON
            color_array[j + 1] = COLOR_COMPARISON
            plt.bar(range(n), data, color=color_array)
            mypause(1)
            plt.clf()  # Grafik temizleme

            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

        # Yer değiştirilen değeri renklendirme
        create_graph()
        color_array = [COLOR_UNSORTED] * n
        color_array[j + 1] = COLOR_SWAP
        plt.bar(range(n), data, color=color_array)
        mypause(1)
        plt.clf()  # Grafik temizleme

        # Sıralanmış ve sıralanmamış elemanları renklendirme
        create_graph()
        color_array = [COLOR_SORTED] * (i + 1) + [COLOR_UNSORTED] * (n - i - 1)
        plt.bar(range(n), data, color=color_array)
        mypause(1)
        plt.clf()  # Grafik temizleme

    plt.ioff()
    print("end")


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
dropdown_algorithm = tk.OptionMenu(frame_left, algorithm, "Seçme Sıralaması", "Kabarcık Sıralaması", "Ekleme Sıralaması")
dropdown_algorithm.pack(pady=5)

label_graph_type = tk.Label(frame_left, text="Grafik Türü:")
label_graph_type.pack()
dropdown_graph_type = tk.OptionMenu(frame_left, graph_type, "Sütun (Bar) Grafiği", "Dağılım (Scatter) Grafiği")
dropdown_graph_type.pack(pady=5)

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
