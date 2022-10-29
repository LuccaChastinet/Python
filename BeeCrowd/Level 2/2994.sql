WITH 
	c_hour_earns AS (VALUES(150)),
	salaries AS (
		
		SELECT
			attendances.id_doctor,
			ROUND(SUM((attendances.hours * (table c_hour_earns)) 
					  + (attendances.hours * (table c_hour_earns) * (work_shifts.bonus/100)))
				  , 1) AS salary
		FROM attendances
		INNER JOIN work_shifts
			ON attendances.id_work_shift = work_shifts.id
		GROUP BY attendances.id_doctor
)
SELECT
	doctors.name,
	salaries.salary
FROM doctors
INNER JOIN salaries
	ON doctors.id = salaries.id_doctor
ORDER BY salary DESC
;
