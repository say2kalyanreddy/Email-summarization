{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf70e224",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\say2k\\onedrive\\desktop\\project\\myenv\\Lib\\site-packages\\tqdm\\auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'summary_text': 'In the serene village of Valebrook, the passing of time seemed to move slower. At the heart of this village stood a quaint workshop, adorned with intricate carvings of gears and celestial bodies. Inside, the soft tick-tock of countless clocks filled the air, each one meticulously crafted by the village’s most esteemed artisan, Elara.'}]\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "# Explicitly specify to use the PyTorch framework\n",
    "summarizer = pipeline(\"summarization\", model=\"facebook/bart-large-cnn\", framework=\"pt\")\n",
    "\n",
    "ARTICLE = \"\"\" In the serene village of Valebrook, the passing of time seemed to move slower, almost as if it respected the quiet and unhurried pace of life there. At the heart of this village stood a quaint workshop, adorned with intricate carvings of gears and celestial bodies. Inside, the soft tick-tock of countless clocks filled the air, each one meticulously crafted by the village’s most esteemed artisan, Elara.\n",
    "\n",
    "Elara was known not just for her craftsmanship, but for the peculiar rumor that her clocks held a secret power: the ability to control time. Though she never confirmed such tales, the villagers often whispered of mysterious happenings that seemed to defy the natural order, all somehow linked to Elara's creations.\n",
    "\n",
    "One crisp autumn morning, a stranger arrived in Valebrook. Young and full of fervor, Aric was an inventor on the cusp of a breakthrough. He had heard of Elara’s legendary clocks and was determined to uncover their secrets. He knocked on her workshop door, his eyes alight with a blend of admiration and ambition.\n",
    "\n",
    "Elara, though wary of the outsider, saw a spark in Aric that reminded her of her younger self. Reluctantly, she agreed to teach him, sensing that his quest was driven by more than mere curiosity. As days turned into weeks, the two worked side by side, their bond growing through shared discoveries and the unspoken understanding of those who walk the path of innovation.\n",
    "\n",
    "One evening, as they pored over ancient blueprints, they stumbled upon a forgotten legend: the Chronos Key. This mythical timepiece was said to possess the power to alter history itself. Intrigued and determined, Elara and Aric set out on a journey to find this artifact, believing it could be the culmination of their work.\n",
    "\n",
    "Their quest led them through enchanted forests, across perilous mountains, and into the depths of hidden caves. Each challenge they faced tested their ingenuity and resolve. They decoded cryptic messages, solved intricate puzzles, and narrowly escaped traps set by those who had sought the Chronos Key before them.\n",
    "\n",
    "After months of searching, they finally stood before the ancient ruins where the key was said to be hidden. Within a dimly lit chamber, they found the timepiece, its intricate design unlike anything they had ever seen. As Elara held it in her hands, she felt the weight of its power and the responsibility that came with it.\n",
    "\n",
    "In that moment, Elara and Aric realized the profound truth of their journey. The true power of time was not in altering it, but in the experiences and memories they had created along the way. With a mutual understanding, they decided to leave the Chronos Key hidden, its secrets intact, and return to Valebrook with a renewed appreciation for the present.\n",
    "\n",
    "Back in her workshop, Elara crafted a new clock, one that symbolized their journey. She presented it to Aric, a reminder that time's true value lies in cherishing every moment. As the village clock chimed, marking the passage of another hour, Elara and Aric knew that they had discovered something far more valuable than any ancient artifact – they had found the essence of time itself. \"\"\"\n",
    "print(summarizer(ARTICLE))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5e559d37",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Token indices sequence length is longer than the specified maximum sequence length for this model (733 > 512). Running this sequence through the model will result in indexing errors\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'summary_text': 'the Chronos Key was said to possess the power to alter history itself . they decoded cryptic messages, solved intricate puzzles, and narrowly escaped traps set by those who had sought it before them . in a dimly lit chamber, they found the clock, its intricate design unlike anything they had ever seen .'}]\n"
     ]
    }
   ],
   "source": [
    "from transformers import pipeline\n",
    "\n",
    "# Explicitly specify to use the PyTorch framework\n",
    "summarizer = pipeline(\"summarization\", model=\"google-t5/t5-small\")\n",
    "\n",
    "ARTICLE = ''' In the serene village of Valebrook, the passing of time seemed to move slower, almost as if it respected the quiet and unhurried pace of life there. At the heart of this village stood a quaint workshop, adorned with intricate carvings of gears and celestial bodies. Inside, the soft tick-tock of countless clocks filled the air, each one meticulously crafted by the village’s most esteemed artisan, Elara.\n",
    "\n",
    "Elara was known not just for her craftsmanship, but for the peculiar rumor that her clocks held a secret power: the ability to control time. Though she never confirmed such tales, the villagers often whispered of mysterious happenings that seemed to defy the natural order, all somehow linked to Elara's creations.\n",
    "\n",
    "One crisp autumn morning, a stranger arrived in Valebrook. Young and full of fervor, Aric was an inventor on the cusp of a breakthrough. He had heard of Elara’s legendary clocks and was determined to uncover their secrets. He knocked on her workshop door, his eyes alight with a blend of admiration and ambition.\n",
    "\n",
    "Elara, though wary of the outsider, saw a spark in Aric that reminded her of her younger self. Reluctantly, she agreed to teach him, sensing that his quest was driven by more than mere curiosity. As days turned into weeks, the two worked side by side, their bond growing through shared discoveries and the unspoken understanding of those who walk the path of innovation.\n",
    "\n",
    "One evening, as they pored over ancient blueprints, they stumbled upon a forgotten legend: the Chronos Key. This mythical timepiece was said to possess the power to alter history itself. Intrigued and determined, Elara and Aric set out on a journey to find this artifact, believing it could be the culmination of their work.\n",
    "\n",
    "Their quest led them through enchanted forests, across perilous mountains, and into the depths of hidden caves. Each challenge they faced tested their ingenuity and resolve. They decoded cryptic messages, solved intricate puzzles, and narrowly escaped traps set by those who had sought the Chronos Key before them.\n",
    "\n",
    "After months of searching, they finally stood before the ancient ruins where the key was said to be hidden. Within a dimly lit chamber, they found the timepiece, its intricate design unlike anything they had ever seen. As Elara held it in her hands, she felt the weight of its power and the responsibility that came with it.\n",
    "\n",
    "In that moment, Elara and Aric realized the profound truth of their journey. The true power of time was not in altering it, but in the experiences and memories they had created along the way. With a mutual understanding, they decided to leave the Chronos Key hidden, its secrets intact, and return to Valebrook with a renewed appreciation for the present.\n",
    "\n",
    "Back in her workshop, Elara crafted a new clock, one that symbolized their journey. She presented it to Aric, a reminder that time's true value lies in cherishing every moment. As the village clock chimed, marking the passage of another hour, Elara and Aric knew that they had discovered something far more valuable than any ancient artifact – they had found the essence of time itself. '''\n",
    "print(summarizer(ARTICLE))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "375b3b35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\say2k\\OneDrive\\Desktop\\Project\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c2b94310",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved email 1.\n",
      "Saved email 2.\n",
      "Saved email 4.\n",
      "Saved email 5.\n",
      "Saved email 6.\n",
      "Saved email 8.\n",
      "Saved email 9.\n",
      "Saved email 10.\n",
      "Saved email 11.\n",
      "Saved email 12.\n",
      "Saved email 14.\n",
      "Saved email 15.\n",
      "Saved email 16.\n",
      "Saved email 18.\n",
      "Saved email 19.\n",
      "Saved email 21.\n",
      "Saved email 23.\n",
      "Saved email 24.\n",
      "Saved email 25.\n",
      "Saved email 26.\n",
      "Saved email 27.\n",
      "Saved email 28.\n",
      "Saved email 30.\n",
      "Saved email 31.\n",
      "Saved email 32.\n",
      "Saved email 35.\n",
      "Saved email 36.\n",
      "Saved email 37.\n",
      "Saved email 38.\n",
      "Saved email 39.\n",
      "All emails have been saved to emails.txt.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import base64\n",
    "import json\n",
    "import re\n",
    "from google.auth.transport.requests import Request\n",
    "from google.oauth2.credentials import Credentials\n",
    "from google_auth_oauthlib.flow import InstalledAppFlow\n",
    "from googleapiclient.discovery import build\n",
    "\n",
    "# If modifying these SCOPES, delete the file token.json.\n",
    "SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']\n",
    "\n",
    "def authenticate_gmail():\n",
    "    \"\"\"Shows basic usage of the Gmail API.\n",
    "    Lists the user's Gmail labels.\n",
    "    \"\"\"\n",
    "    creds = None\n",
    "    # The file token.json stores the user's access and refresh tokens, and is\n",
    "    # created automatically when the authorization flow completes for the first\n",
    "    # time.\n",
    "    if os.path.exists('token.json'):\n",
    "        with open('token.json', 'r') as token:\n",
    "            creds = Credentials.from_authorized_user_file('token.json', SCOPES)\n",
    "    # If there are no (valid) credentials available, let the user log in.\n",
    "    if not creds or not creds.valid:\n",
    "        if creds and creds.expired and creds.refresh_token:\n",
    "            creds.refresh(Request())\n",
    "        else:\n",
    "            flow = InstalledAppFlow.from_client_secrets_file(\n",
    "                'credentials.json', SCOPES)\n",
    "            creds = flow.run_local_server(port=0)\n",
    "        # Save the credentials for the next run\n",
    "        with open('token.json', 'w') as token:\n",
    "            token.write(creds.to_json())\n",
    "    return creds\n",
    "\n",
    "def remove_links(text):\n",
    "    \"\"\"Remove or shorten links in the given text.\"\"\"\n",
    "    # Option 1: Remove links\n",
    "    # text = re.sub(r'http\\S+', '', text)\n",
    "\n",
    "    # Option 2: Shorten links\n",
    "    text = re.sub(r'http\\S+', '[LINK]', text)\n",
    "    \n",
    "    return text\n",
    "\n",
    "def save_emails(service, user_id='me', max_results=10):\n",
    "    # Call the Gmail API to fetch INBOX\n",
    "    results = service.users().messages().list(userId=user_id, maxResults=max_results).execute()\n",
    "    messages = results.get('messages', [])\n",
    "\n",
    "    if not messages:\n",
    "        print('No messages found.')\n",
    "    else:\n",
    "        all_emails_content = \"\"\n",
    "        for i, msg in enumerate(messages):\n",
    "            msg_id = msg['id']\n",
    "            message = service.users().messages().get(userId=user_id, id=msg_id).execute()\n",
    "\n",
    "            # Decode the email message payload\n",
    "            msg_str = \"\"\n",
    "            if 'parts' in message['payload']:\n",
    "                for part in message['payload']['parts']:\n",
    "                    if part['mimeType'] == 'text/plain':\n",
    "                        msg_str += base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')\n",
    "            elif 'body' in message['payload'] and 'data' in message['payload']['body']:\n",
    "                if message['payload']['mimeType'] == 'text/plain':\n",
    "                    msg_str = base64.urlsafe_b64decode(message['payload']['body']['data']).decode('utf-8')\n",
    "\n",
    "            # Remove or shorten links in the email content\n",
    "            msg_str = remove_links(msg_str)\n",
    "\n",
    "            # Append the email content to the combined content string\n",
    "            if msg_str:\n",
    "                all_emails_content += f\"...\\n\\\"{msg_str}\\\"\\n...\\n\\n\"\n",
    "                print(f'Saved email {i+1}.')\n",
    "\n",
    "        # Save all email contents to a single text file\n",
    "        with open('emails.txt', 'w', encoding='utf-8') as email_file:\n",
    "            email_file.write(all_emails_content)\n",
    "        print('All emails have been saved to emails.txt.')\n",
    "\n",
    "def main():\n",
    "    creds = authenticate_gmail()\n",
    "    service = build('gmail', 'v1', credentials=creds)\n",
    "    save_emails(service, max_results=40)  # Change the number to increase the number of emails\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cfc55f9f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Token indices sequence length is longer than the specified maximum sequence length for this model (586 > 512). Running this sequence through the model will result in indexing errors\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n",
      "Your max_length is set to 100, but your input_length is only 57. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=28)\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n",
      "Your max_length is set to 100, but your input_length is only 50. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=25)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved summarized emails to emails_summary.csv.\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import pandas as pd\n",
    "from transformers import pipeline\n",
    "\n",
    "# Initialize the summarizer pipeline\n",
    "summarizer = pipeline(\"summarization\",model=\"google-t5/t5-small\")\n",
    "\n",
    "def extract_emails_from_file(file_path):\n",
    "    \"\"\"Extracts individual emails from the given file content.\"\"\"\n",
    "    with open(file_path, 'r', encoding='utf-8') as file:\n",
    "        content = file.read()\n",
    "    \n",
    "    # Split the content by the email boundaries ...\n",
    "    emails = re.findall(r'\\.\\.\\.\\n\"(.*?)\"\\n\\.\\.\\.', content, re.DOTALL)\n",
    "    return emails\n",
    "\n",
    "def summarize_emails(emails):\n",
    "    \"\"\"Summarizes each email using the summarization pipeline.\"\"\"\n",
    "    summarized_emails = []\n",
    "    for email in emails:\n",
    "        summary = summarizer(email, max_length=100, min_length=30, do_sample=False)[0]['summary_text']\n",
    "        summarized_emails.append(summary)\n",
    "    return summarized_emails\n",
    "\n",
    "def save_to_csv(emails, summarized_emails, output_file):\n",
    "    \"\"\"Saves the original and summarized emails to a CSV file.\"\"\"\n",
    "    data = {\n",
    "        \"Number\": list(range(1, len(emails) + 1)),\n",
    "        \"Original Email\": emails,\n",
    "        \"Summarized Email\": summarized_emails\n",
    "    }\n",
    "    df = pd.DataFrame(data)\n",
    "    df.to_csv(output_file, index=False)\n",
    "\n",
    "def main():\n",
    "    input_file = 'emails.txt'\n",
    "    output_file = 'emails_summary.csv'\n",
    "    \n",
    "    emails = extract_emails_from_file(input_file)\n",
    "    summarized_emails = summarize_emails(emails)\n",
    "    save_to_csv(emails, summarized_emails, output_file)\n",
    "    print(f'Saved summarized emails to {output_file}.')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "110a336e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "import torch\n",
    "print(torch.cuda.is_available())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4fb88232",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Looking in indexes: https://download.pytorch.org/whl/cu117\n",
      "Requirement already satisfied: torch in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (2.3.1)\n",
      "Requirement already satisfied: torchvision in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (0.18.1)\n",
      "Requirement already satisfied: torchaudio in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (2.3.1)\n",
      "Requirement already satisfied: filelock in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (3.14.0)\n",
      "Requirement already satisfied: typing-extensions>=4.8.0 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (4.12.1)\n",
      "Requirement already satisfied: sympy in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (1.12.1)\n",
      "Requirement already satisfied: networkx in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (3.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (3.1.4)\n",
      "Requirement already satisfied: fsspec in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (2024.6.0)\n",
      "Requirement already satisfied: mkl<=2021.4.0,>=2021.1.1 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torch) (2021.4.0)\n",
      "Requirement already satisfied: numpy in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torchvision) (1.26.4)\n",
      "Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from torchvision) (10.3.0)\n",
      "Requirement already satisfied: intel-openmp==2021.* in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from mkl<=2021.4.0,>=2021.1.1->torch) (2021.4.0)\n",
      "Requirement already satisfied: tbb==2021.* in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from mkl<=2021.4.0,>=2021.1.1->torch) (2021.12.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from jinja2->torch) (2.1.5)\n",
      "Requirement already satisfied: mpmath<1.4.0,>=1.1.0 in c:\\users\\say2k\\onedrive\\desktop\\project\\myenv\\lib\\site-packages (from sympy->torch) (1.3.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (myllm)",
   "language": "python",
   "name": "myllm"
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
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
