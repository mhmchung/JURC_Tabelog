-- 👤 Customers（使用者資料）
INSERT INTO customers (nick_name, phone, avatar_url, preference_type)
VALUES
('Paul', '0900000000', 'https://example.com/avatar1.png', 'spicy'),
('Mina', '0911111111', 'https://example.com/avatar2.png', 'vegan');

-- 🔐 Auth accounts（僅 email/password 登入）
-- 密碼假設已經是 bcrypt 加密過的（實務上由後端處理）
INSERT INTO auth_accounts (customer_id, provider, email, password_hash)
VALUES
(1, 'email', 'paul@example.com', '$2b$10$EXAMPLEHASHEDPASSWORD1'),
(2, 'email', 'mina@example.com', '$2b$10$EXAMPLEHASHEDPASSWORD2');

-- 🍽️ 餐廳資料
INSERT INTO restaurants (name, phone_number, location, type, price_range, vibe, average_waiting_time, opening_hours, website_url)
VALUES 
('牛角燒肉', '0223456789', '台北市大安區仁愛路四段', '日式燒肉', '中高', '熱鬧、適合聚餐', 20, '11:00-22:00', 'https://gyukaku.com.tw'),
('素食天國', '0222222222', '新北市板橋區中山路一段', '純素', '中', '安靜、適合獨處', 10, '10:00-21:00', 'https://veganparadise.tw');

-- 🍛 菜色資料
INSERT INTO dishes (restaurant_id, name, type, price, taste, portion, info, is_pr)
VALUES 
(1, '牛五花', '燒肉', 280.00, '油香濃郁', '中份', '搭配蒜片非常對味', FALSE),
(1, '雞軟骨', '燒烤', 150.00, '脆口有嚼勁', '小份', '適合搭配啤酒', FALSE),
(2, '蔬菜咖哩', '主餐', 220.00, '溫和微辣', '大份', '含多種根莖類蔬菜', FALSE),
(2, '豆腐漢堡排', '主餐', 200.00, '清爽淡口', '中份', '搭配特製味噌醬', FALSE);

-- 🌟 餐廳評論
INSERT INTO restaurant_reviews (customer_id, restaurant_id, tasty_score, service_score, ambience_score, comment, visit_time, is_anonymous)
VALUES
(1, 1, 5, 4, 4, '肉質很好，但用餐環境稍微吵雜', '2025-07-20 19:00:00', FALSE),
(2, 2, 4, 5, 5, '安靜舒服，素食菜單很有誠意', '2025-07-21 12:30:00', FALSE);

-- 📝 菜色評論
INSERT INTO dish_reviews (customer_id, restaurant_id, dish_id, score, comment, is_anonymous)
VALUES
(1, 1, 1, 5, '牛五花油花分布完美，推推', FALSE),
(2, 2, 3, 4, '蔬菜咖哩味道不錯，但稍微偏淡', FALSE);
