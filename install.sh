clear
echo ""
echo "This script for generating string session"
echo "        ✥•─────────────────•✥           "
echo "(1) pyrogram"
echo "(2) telethon"
echo "(3) exit"
echo "        ✥•─────────────────•✥           "
read -p "Select: " answer
echo ""
if [ $answer == "1" ]
then
   echo "Pyrogram selected"
   echo "Running script..."
   apt install wget
   pip install pyrogram
   wget https://raw.githubusercontent.com/otseeserver/stringsession/main/pyrostr.py
   clear
   python pyrostr.py

elif [ $answer == "2" ]
then
    echo "Telethon selected"
    echo "Running script..."
    apt install wget
    pip install telethon
    wget https://raw.githubusercontent.com/otseeserver/stringsession/main/telstr.py
    clear
    python telstr.py
elif [ $answer == "3" ]
then
    echo ""
    echo "Thanks for using script"
    exit
    sleep 1
    clear
else
    echo "Please enter again your select"
fi
