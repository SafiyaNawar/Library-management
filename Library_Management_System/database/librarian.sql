CREATE TABLE `lib`.`borrowedby` (
  `borrownum` INT NOT NULL,
  `bnum` INT,
  `issued` DATE,
  `returnd` DATE,
  PRIMARY KEY (`borrownum`),
  FOREIGN KEY (`bnum`) REFERENCES books(`num`),
  FOREIGN KEY (`issued`) REFERENCES report(`issued`),
  FOREIGN KEY (`returnd`) REFERENCES report(`returnd`)
  );
