const TOKEN = process.env.TELEGRAM_TOKEN || 'YOUR_TELEGRAM_BOT_TOKEN';
const gameName = process.env.TELEGRAM_GAMENAME || 'YOUR_TELEGRAM_GAMENAME';
// Specify '0' to use ngrok i.e. localhost tunneling
//let url = process.env.URL || 'https://<PUBLIC-URL>';
const port = process.env.PORT || 8080;

const TelegramBot = require('./node-telegram-bot-api');
const express = require('express');