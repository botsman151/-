{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05c511a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "botsman151/Parsing\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import json\n",
    "\n",
    "params = {'q': 'name', 'id': '69846294'}\n",
    "\n",
    "url = 'https://api.github.com'\n",
    "\n",
    "user = 'botsman151'\n",
    "\n",
    "responce = requests.get(f'{url}/users/{user}/repos')\n",
    "\n",
    "with open('data.json', 'w') as f:\n",
    "    json.dump(responce.json(), f)\n",
    "\n",
    "for i in responce.json():\n",
    "    print(i['full_name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53604dc2",
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
