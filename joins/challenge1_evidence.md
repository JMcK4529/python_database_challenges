# Joins 1
## Exercise 1
### Input
```sql
SELECT albums.id, albums.title
FROM albums JOIN artists
ON artists.id = albums.artist_id
WHERE artists.name = 'Taylor Swift';
```
### Output
```
 id |  title   
----+----------
  6 | Lover
  7 | Folklore
(2 rows)
```
## Exercise 2
### Input
```sql
SELECT albums.id, albums.title
FROM albums JOIN artists
ON artists.id = albums.artist_id
WHERE artists.name = 'Pixies' AND albums.release_year = 1988;
```
### Output
```
 id |    title    
----+-------------
  2 | Surfer Rosa
(1 row)
```
## Challenge
### Input
```sql
SELECT albums.id, albums.title
FROM albums JOIN artists
ON artists.id = albums.artist_id
WHERE artists.name = 'Nina Simone' AND albums.release_year > 1975;
```
### Output
```
 id |       title        
----+--------------------
  9 | Baltimore
 11 | Fodder on My Wings
(2 rows)
```