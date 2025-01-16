import sqlite3 as sq

with sq.connect('health_life.db', check_same_thread=False) as health_life:
    health_life.executescript("""
    
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER INTEGER PRIMARY KEY AUTOINCREMENT,      -- ID каждого пользователя по программе
        user_id INTEGER,                                   -- ID пользователя в телеграмме
        user_name TEXT,                                     -- имя пользователя по телеграмм
        first_name TEXT                                     -- логин пользователя
       );
    
    CREATE TABLE IF NOT EXISTS people(
        people_id INTEGER PRIMARY KEY,       -- id параметров каждого пользователя
        user_id INTEGER,                            -- id пользователя в телегамме
        weight INTEGER,                             -- вес пользователя
        height INTEGER,                             -- рост пользователя
        age INTEGER,                                -- возраст пользователя 
        gender CHAR,                                -- пол пользователя
        datetime DATE                               -- дата ввода информации   
        );

    CREATE TABLE IF NOT EXISTS trenerovka(
        req_id INTEGER PRIMARY KEY NOT NULL,            -- номер записи
        user_id INTEGER,                                -- id номер пользователя
        muscless TEXT,                                  -- название мускула для укрепления
        equipment TEXT,                                 -- упражнения
        explaination TEXT,  
        long_explanation TEXT,
        video TEXT
        );
        
    CREATE TABLE IF NOT EXISTS history(
        history_id INTEGER PRIMARY KEY NOT NULL,
        user_id INTEGER,
        muscless TEXT,
        trenerovka_id INTEGER,
        sets TEXT,
        date DATETIME
    );
    """)
