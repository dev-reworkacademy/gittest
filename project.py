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

def get_most_watched_by_gender():

    customers = read_file("customers.csv").split("\n")
    male_genre = []
    female_genre = []

    for customer in customers:
        if customer != "":
            columns = customer.split(",")
            
            if columns[2].lower() == "m":
                male_genre.append(customer)

            if columns[2].lower() == "f":
                female_genre.append(customer)

    arr = []
    for customer in male_genre:
        columns = customer.split(",")
        genre = columns[3].split("-")
        arr.extend(genre)
    
    most_watched_by_male = max_freq(arr)

    arr = []
    for customer in female_genre:
        columns = customer.split(",")
        genre = columns[3].split("-")
        arr.extend(genre)

    most_watched_by_female = max_freq(arr)

    return most_watched_by_male,most_watched_by_female


def most_watched_genre():
    customers = read_file("customers.csv").split("\n")
    arr = []
    for customer in customers:
        if customer != "":
            columns = customer.split(",")
            genre = columns[3].split("-")
            arr.extend(genre)
    
    return max_freq(arr)

def max_freq(arr):
    freq = {}
    genres = []

    try:
        for  i in arr:
            if freq.get(i):
                freq[i] += 1
            else:
                freq[i] = 1
            # this is simplified version of the algorithm above
            # freq[i] = freq.get(i,0) + 1
    except:
        pass

    values = freq.values()
    max_value = max(values)

    for key,value in freq.items():
        if(value == max_value):
            genres.append(key)
    # [2,1,2,1,1]
    return genres


def analyze():
    most_watched = ','.join(most_watched_genre())
    print(f"Most watched genre: {most_watched}")

    male_value,female_value = get_most_watched_by_gender()
    male_genre = ','.join(male_value)
    female_genre = ','.join(female_value)

    print(f"Most watched genre by male: {male_genre}")
    print(f"Most watched genre by female: {female_genre}")

    get_most_watched_by_gender()
    

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