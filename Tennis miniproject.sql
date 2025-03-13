select * from tennis_miniproject.comp_data;
SELECT competition_name ,category_name
from tennis_miniproject.comp_data;
SELECT category_name, COUNT(competition_name) AS competition_count
FROM tennis_miniproject.comp_data
GROUP BY category_name;
SELECT competition_name, category_name
FROM tennis_miniproject.comp_data
WHERE type = 'Doubles';
SELECT competition_name, category_name
FROM tennis_miniproject.comp_data
WHERE category_name = 'ATP';
SELECT 
    parent.competition_name AS parent_competition,
    sub.competition_name AS sub_competition
FROM 
    tennis_miniproject.comp_data AS parent
LEFT JOIN 
    tennis_miniproject.comp_data AS sub ON parent.competition_name = sub.parent_id
WHERE 
    parent.parent_id IS NULL;
    SELECT 
    category_name, 
    type, 
    COUNT(*) AS competition_count
FROM 
    tennis_miniproject.comp_data
GROUP BY 
    category_name, 
    type
ORDER BY 
    category_name, 
    type;
SELECT competition_name, type, gender, category_id, category_name, level
FROM tennis_miniproject.comp_data
WHERE parent_id IS NULL;


