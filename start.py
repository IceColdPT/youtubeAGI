import os
import json
import openai



chan_folder_name = "chan"

current_folder = os.getcwd()
chan_folder_path = os.path.join(current_folder, chan_folder_name)



def get_setting(name):
    with open(os.path.join(current_folder,"settings.json"), 'r') as file:
            data = json.load(file)
            if name in data:
                return data[name]
            else:
                return f"Key '{name}' not found in the JSON file."
            
openai.api_key = get_setting("openai")

def main():
    # Check how many folders exist in chan_folder_path

    try:
        items_in_path = os.listdir(chan_folder_path)
    except:
        items_in_path = []
    count = len(items_in_path)
    selected_option = 0
    max_options = 0
    if count > 0:
        for fn in items_in_path:
            print("{0}) {1}".format(max_options, fn)) 
            max_options += 1
    print("{0}) create new chan".format(max_options))  
    option = input("Choose your option:  ")
    if option.isnumeric() and int(option) <= max_options:  
        if option == str(max_options):  
            create_new_chan()
        else:
            select_chan(items_in_path[int(option)])  # Fixed the selection of the channel name
    else:
        print("You must choose a correct option!!\n")
        main()

def create_new_chan():
    chan_name = input("\nWhat is the chan name? :")
    if chan_name == "":
        print("Name cannote be empty!\n")
        create_new_chan()
    else:
        print("creating channel: " + chan_name+"\n")
        try:
            os.makedirs(os.path.join(chan_folder_path,chan_name))
            print(f"Folder '{chan_name}' created successfully.")
            main()
        except OSError as e:
            print(f"An error occurred: {e}")
            main()

def select_chan(name):
    print("Selected channel: " + name)
    create_new_video(name)
    

def create_new_video(chanName):
    name = input("\n\rYou are creating a new video. What is the name of the video?")
    description = input("\n\r what is the description of the video? be specific!")
    niche = input("\n\rWrite, between ',' who is the target audience of this video")
    video_name = name.replace(" ","_")
    os.makedirs(os.path.join(chan_folder_path,chanName,video_name))
    create_and_write_txt_file(os.path.join(chan_folder_path,chanName,video_name),"name.txt",name)
    create_and_write_txt_file(os.path.join(chan_folder_path,chanName,video_name),"description.txt",description)
    create_and_write_txt_file(os.path.join(chan_folder_path,chanName,video_name),"niche.txt",niche)




def create_and_write_txt_file(folder_path, file_name, content):
    try:
        # Combine the folder path and file name
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'w+') as file:
            file.write(content)
        print(f"File '{file_name}' created in '{folder_path}' and content written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    main()
