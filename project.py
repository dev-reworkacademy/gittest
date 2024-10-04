def read_file(file):
    with open(file) as f:
        return f.read()

def save_customer_info(file, content):
    with open(file,"a") as f:
        f.write(content+"\n")
    print("Customer saved")

def read_genre():
    arr = []
    content = read_file('genre.txt').split("\n")
    for i in content:
        if i != "":
            i = i.capitalize()
            arr.append(i)
    return arr

def display_genre():
    count  = 1
    content = read_genre()
    for i in content:
      
        print(f"{count}. {i}")
        count = count + 1

def get_genre_selection(options):
    genre_option = options.split(",")
    genres = read_genre()

    arr = []
    for i in genre_option:
        index = int(i) - 1
        option = genres[index]
        arr.append(option)

    return arr


def create_user():
    name =  input("Enter your name:")
    age = input("Enter your age:")
    gender = input("Enter your gender:")

    eq = "-" * 20
    print(eq)
    display_genre()
    print(eq)
    genre =  input("Select at least 3. Example 1,2,3:")

    selection = get_genre_selection(genre)
    genres = '-'.join(selection)

    data =  f"{name},{age},{gender},{genres}"
    save_customer_info("customers.csv",data)


def most_watched_genre():
    customers = read_file("customers.csv").split("\n")
    arr = []
    for customer in customers:
        if customer != "":
            columns = customer.split(",")
            genre = columns[3].split("-")
            arr.extend(genre)
    
    print(max_freq(arr))

def max_freq(arr):
    freq = {}
    try:

        for  i in arr:
            # if(freq.get(i)):
            freq[i] += 1
    except:
        pass
        # else:
        #     freq[i] = 1

    # [2,1,2,1,1]
    return freq

def analyze():
    most_watched_genre()
    

def display():
    print("1. Create new user")
    print("2. Analyze")
    print("3. Exit program")

    option  = input("Select from 1-3:")

    if option == "1":
        create_user()
    elif option == "2":
        analyze()
    else:
        exit()

display()