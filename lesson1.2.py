{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9abbb53b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import json\n",
    "\n",
    "app_id = 4106804\n",
    "vk_version = '5.131'\n",
    "access_token = input('\\nВведите токен доступа: ')\n",
    "\n",
    "response = requests.get(f'https://api.vk.com/method/groups.get?extended=1&access_token={access_token}&v={vk_version}')\n",
    "response_json = response.json()\n",
    "with open('lesson1.2.json', 'w') as file:\n",
    "    json.dump(response_json, file)\n",
    "\n",
    "print('\\nСписок сообществ, на которые вы подписаны')\n",
    "for group in response_json['response']['items']:\n",
    "    print(f\"{group['name']}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abb11a6f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
