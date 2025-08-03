-- 🧑‍💻 顧客主檔：個人資訊（不含登入資料）
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    nick_name VARCHAR(50),
    phone VARCHAR(20),
    avatar_url TEXT,
    basic_info TEXT,
    preference_type VARCHAR(50),
    churn_rate REAL DEFAULT 0,
    review_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active_at TIMESTAMP
);

-- 🔐 登入帳號資料：支援多種登入方式（email/password、Google、Apple…）
CREATE TABLE auth_accounts (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id) ON DELETE CASCADE,
    provider VARCHAR(50) NOT NULL,           -- 'email', 'google', 'apple' 等
    provider_id VARCHAR(100),                -- 第三方帳號識別，如 Google sub
    email VARCHAR(100),
    password_hash TEXT,                      -- 僅 email/password 登入使用
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(provider, provider_id),           -- ex: 一個 Google 帳戶只能綁一個帳號
    UNIQUE(email, provider)                  -- email 登入需唯一
);

-- 🍽️ 餐廳主檔
CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20),
    location TEXT,
    accessibility TEXT,
    parking BOOLEAN DEFAULT FALSE,
    type VARCHAR(50),
    price_range VARCHAR(50),
    vibe TEXT,
    average_waiting_time INTEGER, -- 單位：分鐘
    online_reservation BOOLEAN DEFAULT FALSE,
    opening_hours TEXT,
    website_url TEXT,
    menu_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🧆 菜色資料
CREATE TABLE dishes (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50),
    price NUMERIC(10, 2),
    taste TEXT,
    portion TEXT,
    info TEXT,
    is_pr BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🌟 餐廳評論
CREATE TABLE restaurant_reviews (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id) ON DELETE SET NULL,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants(id) ON DELETE CASCADE,
    tasty_score INTEGER CHECK (tasty_score BETWEEN 1 AND 5),
    service_score INTEGER CHECK (service_score BETWEEN 1 AND 5),
    ambience_score INTEGER CHECK (ambience_score BETWEEN 1 AND 5),
    comment TEXT,
    visit_time TIMESTAMP,
    is_anonymous BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (customer_id, restaurant_id, visit_time)
);

-- 📝 菜色評論
CREATE TABLE dish_reviews (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id) ON DELETE SET NULL,
    restaurant_id INTEGER NOT NULL REFERENCES restaurants(id) ON DELETE CASCADE,
    dish_id INTEGER NOT NULL REFERENCES dishes(id) ON DELETE CASCADE,
    score INTEGER CHECK (score BETWEEN 1 AND 5),
    comment TEXT,
    is_anonymous BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (customer_id, dish_id)
);

-- 🔍 常用搜尋索引（建議）
CREATE INDEX idx_auth_accounts_email_provider ON auth_accounts(email, provider);
CREATE INDEX idx_restaurants_name ON restaurants(name);
CREATE INDEX idx_dishes_name ON dishes(name);
CREATE INDEX idx_reviews_customer_id ON restaurant_reviews(customer_id);
CREATE INDEX idx_dish_reviews_customer_id ON dish_reviews(customer_id);
