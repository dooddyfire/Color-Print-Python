from termcolor import cprint 
from pyfiglet import figlet_format,FigletFont


#ปริ้นสี ร่วมกับ AsciiFont ของ PyFiglet
cprint(figlet_format('QRCode',font="slant"),'magenta',attrs=['bold'])

#คำสั่งดูฟ้อนทั้งหมดของ PyFiglet
print(FigletFont.getFonts())

#ปริ้นธรรมดา
print('This is my first program')

#ปริ้นสี
cprint('This is my first program','cyan',attrs=['bold','underline'])

