import threading

from pyrogram import Client, filters, idle

api_id = 168894969
api_hash = "092cda824d1958f6bdbb6aa46500a5b5"


app = Client("my_account", api_id=api_id, api_hash=api_hash)
# class Akin():
#     def __call__(self, s=0):
#         while True:  # making a loop
#             try:  # used try so that if user pressed other than the given key error will not be shown
#                 if keyboard.is_pressed('q'):  # if key 'q' is pressed
#                     # print('You Pressed A Key!')
#                     screenshot = pyscreenshot.grab()
#
#                     # Сохранение изображения.
#                     screenshot.save("screenshot.png")
#                     # app.start()
#                     app.send_document(1598209040, 'screenshot.png')
#                     print('Ok')
#             except Exception as e:
#                 pass
class Akin1():
    def __call__(self, s=0):
        while True:
            try:
                a = input()
                if 'file' in a:
                    app.send_document(5337729489, a[5:])
                app.send_message(5337729489, a)
            except:
                pass

# ccc = Akin()
#
# t100 = threading.Thread(target=ccc)
cc = Akin1()

t10 = threading.Thread(target=cc)
# t100.start()

t10.start()
@app.on_message(filters.user(5337729489))
async def on_message(client, message):
    if message.document:
        await app.download_media(message)
    else:
        print(message.text)

app.run()
  # if user pressed a key other than the given key the loop will break