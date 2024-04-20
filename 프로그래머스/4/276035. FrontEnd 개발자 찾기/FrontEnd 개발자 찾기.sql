SELECT DISTINCT B.ID, B.EMAIL, B.FIRST_NAME, B.LAST_NAME
FROM (SELECT CODE FROM SKILLCODES WHERE CATEGORY='Front End') A, DEVELOPERS B
WHERE B.SKILL_CODE & A.CODE
ORDER BY ID ASC