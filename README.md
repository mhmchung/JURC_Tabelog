# JURC_Tabelog

# Updates
- v0.2 : TBD

- v0.1 (250417): 
	Convert to React due to an unsolvable platform dependency of Vue. Had the logo inplace and did some basic styling. Anything about frontend can start from here. Now switching attention to backend dev.

- v0.0 (250310): 
	Init template structure done. 

# Features
- Table Schemas
	- restaurants
		- name
		- profile
		- id
		- address
		- category (小吃, 高級餐廳, 女僕店)
		- rating
	- rating (below)
	- customers
		- name
		- id
	- dishes
		- name
		- id
	- bookings
	- payments
	- 



- Rating System
	- Dynamic weight
		- user defined vs category fixed weight
	- columns 
		- tasty 
		- cleanliness  
		- services
		- c/p value
		- access
		- vibe
	- promotion system(TBD)
	- coupons system
	- badge system (achievement for customer)



- Booking System
	- TBD
	- Notes
		- Weighting line



- Data Science Topics
	- Exporting reports
	- Data manipulation
	- Recommendation System



- Other Topics
	- Verification to prove real customer experience
		- QR code
		- ...
	- Security Control 

# Command note
```bash
docker-compose up --build -d
docker-compose restart frontend
```