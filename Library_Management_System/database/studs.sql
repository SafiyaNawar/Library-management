/*
-- Query: SELECT * FROM lib.studs
LIMIT 0, 1000

-- Date: 2022-11-20 11:48
*/
INSERT INTO `` (`sid`,`name`,`address`,`phone`,`expiry`,`mem`) VALUES (401,'Rory gilmore','stars hollow',785412369,'2022-11-30','Yes');
INSERT INTO `` (`sid`,`name`,`address`,`phone`,`expiry`,`mem`) VALUES (402,'Jess Meriano','new york',852147896,'2022-11-30','Yes');




CREATE TABLE `lib`.`reports` ( 
  `repnum` INT NOT NULL,
  `sname` VARCHAR(45) NOT NULL,
  `bnum` INT NOT NULL,
  `sid` INT NOT NULL,
  `issue` DATE NOT NULL,
  `return` DATE NOT NULL,
  PRIMARY KEY (`repnum`),
  FOREIGN KEY (bnum) REFERENCES books(num),
  FOREIGN KEY (sid) REFERENCES studs(sid)
  );

