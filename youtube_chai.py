import sqlite3


conn = sqlite3.connect('youtube.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS youtube(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar NOT NULL,
                time text NOT NULL
                )
              ''')
def list_all_video():
    cursor.execute('SELECT * FROM youtube')
    conn.commit()
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO youtube (name, time) VALUES (?, ?)",(name,time))
    conn.commit()

def update_video(id,name,time):
    cursor.execute('UPDATE youtube SET name = ?,time = ? WHERE id = ?',(name,time,id))
    conn.commit()


def delete_video(id):
    cursor.execute("DELETE FROM youtube WHERE id = ?",(id,))
    conn.commit()





def main():
    while True:
        print('''
        1 List All videos
        2. add videos
        3. update videos
        4. delete videos
        5. Exit   ''')
        choose=input("Enter your choice")


        match choose:
            case '1':
                list_all_video()
            case '2':
                name = input("Enter video name")
                time = input("Enter Duration of video")
                add_videos(name,time)
            case '3':
                list_all_video()
                update_id=int(input("Enter video id"))
                name = input("Enter video name")
                time = input("Enter Duration of video")
                update_video(id,name,time)
            case '4':
                list_all_video()
                id = input(" Enter video id")
                delete_video(id)
            case '5':
                break
            case _:
                print("Invalid input")

    conn.close()


if __name__ == "__main__":
    main()
