from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from config import TOKEN
import keyboards as kb

class States(StatesGroup):
    passportstate = State()
    selfiepassportstate = State()
    screenstate = State()
    finishstate = State()


bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

#обрабатываем команду старт от юзера
@dp.message_handler(commands=['start'], state=None)
async def process_frst_lvl(message: types.Message):

    dogovor = open('/home/donotblamepls/PycharmProjects/botosoba/dogovor.jpg', 'rb')

    await bot.send_message(message.from_user.id, "привет, блаблабла, вот договор ответь да, если согласен.")
    await bot.send_photo(message.from_user.id, dogovor, reply_markup=kb.menukb1)

@dp.callback_query_handler(lambda c: c.data == 'mybtn1')
async def btnprocessing(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "пришли мне фото паспорта (картинка образца)")
    obrazec = open('/home/donotblamepls/PycharmProjects/botosoba/obrazec.png', 'rb')
    await bot.send_photo(callback_query.from_user.id, obrazec)
    await States.passportstate.set()

    @dp.message_handler(content_types=['photo'], state=States.passportstate)
    async def handle_docs_photo1(message: types.Message):
        path = ('/home/donotblamepls/PycharmProjects/botosoba/pics from bot/')
        fotopassporta = ('фото паспорта.jpg')
        firstname = message.from_user.first_name
        surname = message.from_user.last_name
        await message.photo[-1].download(path+'/'+firstname+' '+surname+'/'+fotopassporta)
        await bot.send_message(message.from_user.id,"Фотка ОК?", reply_markup=kb.menukb2)


    @dp.callback_query_handler(lambda c: c.data == 'okbtn', state=States.passportstate)
    async def btnprocessing(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
        await bot.send_message(callback_query.from_user.id, "теперь пришли мне селфи с паспортом (картинка)")
        obrazec1 = open('/home/donotblamepls/PycharmProjects/botosoba/obrazec1.jpg', 'rb')
        await bot.send_photo(callback_query.from_user.id, obrazec1)
        await States.selfiepassportstate.set()

    @dp.callback_query_handler(lambda c: c.data == 'povtorbtn', state=States.passportstate)
    async def btnprocessing(callback_query: types.CallbackQuery):
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
        await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 1)
        # нажание кнопки удаляет два последних сообщения в чате
        await bot.send_message(callback_query.from_user.id, "скинь фотку ещё раз")

@dp.message_handler(content_types=['photo'], state=States.selfiepassportstate)
async def handle_docs_photo2(message):
    path = ('/home/donotblamepls/PycharmProjects/botosoba/pics from bot/')

    fotoselfiepassport = ('фото селфи с паспортом.jpg')
    firstname = message.from_user.first_name
    surname = message.from_user.last_name
    await message.photo[-1].download(path + '/' + firstname + ' ' + surname + '/' + fotoselfiepassport)
    await bot.send_message(message.from_user.id, "Селфи с паспортом ок?", reply_markup=kb.menukb3)

@dp.callback_query_handler(lambda c: c.data == 'okbtn1', state=States.selfiepassportstate)
async def btnprocessing(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
    await bot.send_message(callback_query.from_user.id, "теперь переведи мне денег Х по реквизитам Y и скинь скрин")
    await States.screenstate.set()

    @dp.message_handler(content_types=['photo'], state=States.screenstate)
    async def handle_docs_photo3(message):
        path = ('/home/donotblamepls/PycharmProjects/botosoba/pics from bot/')

        paymentscreen = ('скрин оплаты.jpg')
        firstname = message.from_user.first_name
        surname = message.from_user.last_name
        await message.photo[-1].download(path + '/' + firstname + ' ' + surname + '/' + paymentscreen)
        await bot.send_message(message.from_user.id, "Всё верно?", reply_markup=kb.menukb4)

@dp.callback_query_handler(lambda c: c.data == 'povtorbtn1', state=States.selfiepassportstate)
async def btnprocessing(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 1)
    # нажание кнопки удаляет два последних сообщения в чате
    await bot.send_message(callback_query.from_user.id, "скинь фотку ещё раз")

@dp.callback_query_handler(lambda c: c.data == 'okbtn2', state=States.screenstate)
async def btnprocessing(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
    await bot.send_message(callback_query.from_user.id, "Спасибо, вот инструкция по заселению. Вся необходимая информация принята. Ожидай.")
    instruction = open('/home/donotblamepls/PycharmProjects/botosoba/instruction.png', 'rb')
    await bot.send_photo(callback_query.from_user.id, instruction)
    await States.finishstate.set()

    path = ('/home/donotblamepls/PycharmProjects/botosoba/pics from bot/')
    firstname = callback_query.from_user.first_name
    surname = callback_query.from_user.last_name
    fotopassporta = open(path + firstname + ' ' + surname + '/' + 'фото паспорта.jpg', 'rb')
    fotoselfiepassport = open(path + firstname + ' ' + surname + '/' + 'фото селфи с паспортом.jpg', 'rb')
    paymentscreen = open(path + firstname + ' ' + surname + '/' + 'скрин оплаты.jpg', 'rb')

    await bot.send_message(chat_id=5179616968, text='Тут клиент подъехал')
    await bot.send_photo(chat_id=5179616968, photo=fotopassporta)
    await bot.send_photo(chat_id=5179616968, photo=fotoselfiepassport)
    await bot.send_photo(chat_id=5179616968, photo=paymentscreen)

@dp.callback_query_handler(lambda c: c.data == 'povtorbtn2', state=States.screenstate)
async def btnprocessing(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 0)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id - 1)
    # нажание кнопки удаляет два последних сообщения в чате
    await bot.send_message(callback_query.from_user.id, "скинь скрин ещё раз")

    @dp.message_handler(state=States.finishstate)
    async def finishhandler(message: types.Message):
        await message.answer(text='Вся необходимая информация принята. Ожидай.')

if __name__ == '__main__':
    executor.start_polling(dp)