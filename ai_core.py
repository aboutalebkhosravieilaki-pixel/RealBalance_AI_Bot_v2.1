
import numpy as np, random, time, logging
from datetime import datetime, timedelta
from cachetools import TTLCache

class HybridAI:
    def __init__(self):
        self.cache_prices = TTLCache(maxsize=100, ttl=300)
        self.confidence_base = 80
        self.noise_threshold = 0.15

    def get_signal(self):
        try:
            last_prices = np.random.normal(0, 1, 10)
            if np.std(last_prices) > self.noise_threshold:
                return {'signal': 'عدم معامله (نویز بالا)', 'confidence': 0, 'risk': 'بالا'}

            # شبیه‌سازی سیگنال ترکیبی
            direction = random.choice(['خرید', 'فروش'])
            confidence = np.clip(self.confidence_base + np.random.randn() * 5, 50, 99)
            risk = 'کم' if confidence > 80 else 'متوسط'
            return {'signal': direction, 'confidence': int(confidence), 'risk': risk}
        except Exception as e:
            logging.error(f'Model Error: {e}')
            return {'signal': 'خطا', 'confidence': 0, 'risk': 'نامشخص'}

    def retrain_daily(self, new_data=None):
        # بازآموزی روزانه ساده‌شده
        self.confidence_base = np.clip(self.confidence_base + np.random.randn(), 70, 90)

    def feedback_cycle(self, fb):
        if '✅' in fb:
            self.confidence_base = min(98, self.confidence_base + 1)
        elif '❌' in fb:
            self.confidence_base = max(60, self.confidence_base - 1)
