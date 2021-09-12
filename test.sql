SELECT Номер_ВСП, Платеж
FROM CreditCardInfo p 
WHERE Платеж = (SELECT max(Платеж) FROM CreditCardInfo m WHERE p.Номер_ВСП = m.Номер_ВСП) 
ORDER BY Платеж desc;

SELECT CreditCardInfo.Номер_договора_WAY4, CreditCardInfo.ФИО, CreditCardInfo.Номер_карты, CreditCardUploads.Кредитный лимит
FROM CreditCardInfo
     		full outer join CreditCardUploads
on CreditCardInfo.Номер_договора_WAY4 = CreditCardUploads.Номер_договора_WAY4;

SELECT Номер_карты 
FROM CreditCardInfo 
WHERE Номер_ВСП = (SELECT Номер_ВСП FROM CreditCardInfo WHERE Паспортные_данные = '12 34 567890');

CREATE [OR REPLACE] PROCEDURE test
      (report_day IN date)
       
BEGIN
       SELECT Дата_платежа 
       FROM CreditCardInfo 
       WHERE 
             Дата_платежа = to_date(report_day, 'dd.mm.yyyy') 
             and Дата_платежа = to_date(report_day, 'dd.mm.yyyy') - 7 
             and Дата_платежа = to_date(report_day, 'dd.mm.yyyy') - 14 
             and to_date(report_day, 'dd.mm.yyyy') – 21

END test;
