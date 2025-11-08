        import telebot, json, threading, logging
        from ai_core import HybridAI
        from datetime import datetime

        with open('config.json', 'r') as f:
            config = json.load(f)

        bot = telebot.TeleBot(config['TELEGRAM_TOKEN'])
        ai_core = HybridAI()

        logging.basicConfig(filename='errors.log', level=logging.ERROR)

        @bot.message_handler(commands=['start'])
        def start(msg):
            bot.reply_to(msg, '🤖 خوش آمدید به ربات RealBalance!
سیگنال‌ها به صورت هوشمند و با دقت بالا ارسال خواهند شد.')

        @bot.message_handler(commands=['signal'])
        def signal_cmd(msg):
            try:
                prediction = ai_core.get_signal()
                response = f"💰 سیگنال: {prediction['signal']}
🎯 اطمینان: {prediction['confidence']}%
⚠️ ریسک: {prediction['risk']}"
                bot.reply_to(msg, response)
            except Exception as e:
                logging.error(f"Signal Error: {str(e)}")
                bot.reply_to(msg, '❌ خطایی در تولید سیگنال رخ داد.')

        @bot.message_handler(commands=['feedback'])
        def feedback(msg):
            ai_core.feedback_cycle(msg.text)
            bot.reply_to(msg, '✅ بازخورد شما ثبت شد و در یادگیری مدل استفاده خواهد شد.')

        print('🤖 RealBalance_AI_Bot_v2.1 is running...')
        bot.infinity_polling()
