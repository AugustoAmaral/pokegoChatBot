FROM python
RUN apt update && apt upgrade -y && git clone https://github.com/AugustoAmaral/pokegoChatBot.git && cd pokegoChatBot/ && python -m pip install -r requirements.txt && git config --global user.email "guto_wow@hotmail.com" && git config --global user.name "server"
RUN python /pokegoChatBot/autobackup.py & python /pokegoChatBot/launcher.py