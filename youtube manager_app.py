import json

class youtube:
    def __init__(self):
        self.videos=[]

    def load_data(self):
        try:
            with open("youtube.txt","r") as file:
                test=json.load(file)
                return test
        except FileNotFoundError:
            return []
    def test(self,video):
        self.videos=video
    def save_data_helper(self):
        with open("youtube.txt","w") as file:          #
            json.dump(self.videos,file)
    def add_video(self):
        name=input("enter video name: ")
        time=input("enter video length: ")
        self.videos.append({"name":name,"time":time})
        self.save_data_helper()
    def update_video(self):
        self.list_video()
        num=int(input("enter number of video to update: "))
        if 0<num<len(self.videos):
            name=input("enter new video name: ")
            time=input("enter time of new video: ")
            self.videos[num-1]={"name":name,"time":time}
            self.save_data_helper()
        else:
            print("invalid input !")
    def delete_video(self):
        index=int(input("enter number of video to delete: "))
        self.videos.pop(index-1)
    def list_video(self):
        print("\n","*"*30)
        for index,video in enumerate(self.videos,start=1):
            print(f"{index} , {video["name"]} , {video["time"]}")
        print("*"*30)



def main():
    obj=youtube()
    video=obj.load_data()
    obj.test(video)
    while True:
        print("\ngiven functionality: ")
        print("1. List all videos")
        print("2. Add video")
        print("3. update video")
        print("4. Delete Video")
        print("5. exit")
        choice=input("Enter your choice: ")
        match choice:
            case "1":
                obj.list_video()
            case "2":
                obj.add_video()
            case "3":
                obj.update_video()
            case "4":
                obj.delete_video()
            case "5":
                break
            case _:
                print("invalid choice !")


if __name__=="__main__":
    main()