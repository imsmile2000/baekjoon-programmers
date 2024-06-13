SELECT A.ID, B.FISH_NAME, C.LENGTH
FROM FISH_INFO A JOIN FISH_NAME_INFO B ON A.FISH_TYPE=B.FISH_TYPE
JOIN (SELECT FISH_TYPE, MAX(LENGTH) AS LENGTH FROM FISH_INFO GROUP BY FISH_TYPE) C
ON A.LENGTH=C.LENGTH AND B.FISH_TYPE=C.FISH_TYPE
ORDER BY A.ID ASC