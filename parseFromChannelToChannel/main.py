from telethon import TelegramClient, events
phone = input("Ввести номер вашего телеграмма в формате +380...: ")
api_id = input(
    "Ввести api_id вашего телеграмма (Эти данные можно получить перейдя по ссылке https://my.telegram.org): ")
api_hash = input(
    "Ввести api_hash вашего телеграмма (Эти данные можно получить перейдя по ссылке https://my.telegram.org): ")
id1 = input("Ввести ID чата откуда парсить информацию: ")
id2 = input("Ввести ID чата куда парсить информацию: ")



client = TelegramClient(phone, api_id, api_hash)
client.start()


# при появлении нового сообщения в чате, айди чата, из которого берем публикацию
@client.on(events.NewMessage(int(id1)))
async def main(event):
    mas = event.message
    # айди чата, в который отправляем публикацию
    await client.send_message(int(id2), mas)
    msg = mas.message + "\n" + str(mas.date) + "\n\n\n"
    open("data.txt", "a", encoding="utf-8").write(msg)
client.run_until_disconnected()

print('Статус: Успех!')
