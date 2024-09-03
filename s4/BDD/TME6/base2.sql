-- LI2009 BD

-- création de la base FOOFLE

-- syntaxe pour H2

DROP TABLE distance if exists;
DROP TABLE match if exists;
drop table Sponsorise if exists;
drop table Joueur if exists; 
drop table Equipe if exists;

CREATE TABLE Equipe (
NEq VARCHAR2(9) PRIMARY KEY,
Ville VARCHAR2(10) NOT NULL,
Couleur VARCHAR2(8),
StP VARCHAR2(10) NOT NULL);

CREATE TABLE Joueur (
NJo VARCHAR2(15) PRIMARY KEY,
Eq VARCHAR2(9) NOT NULL ,
Taille INT,
Age INT,
CONSTRAINT fkjoueur FOREIGN KEY (Eq) REFERENCES Equipe(NEq));

CREATE TABLE Sponsorise (
NSp VARCHAR2(15),
NJo VARCHAR2(15),
Somme INT,
PRIMARY KEY (NSp,NJo),
CONSTRAINT fksponsorise FOREIGN KEY (NJo) REFERENCES Joueur(NJo));

CREATE TABLE Match (
Eq1 VARCHAR2(9) NOT NULL,
Eq2 VARCHAR2(9) NOT NULL,
DateM DATE,
St  VARCHAR2(10) NOT NULL,
PRIMARY KEY (eq1,eq2),
 FOREIGN KEY (Eq1) REFERENCES Equipe(NEq),
 FOREIGN KEY (Eq2) REFERENCES Equipe(NEq) );

CREATE TABLE Distance (
St1 VARCHAR2(10) NOT NULL,
St2 VARCHAR2(10) NOT NULL,
Nbkm INT,
PRIMARY KEY (St1,St2));

-- /* mettre préalablement le bon format de date */
-- alter session set nls_date_format='yyyy-mm-dd';


-- /* insertions dans la table Equipe */
INSERT INTO Equipe VALUES('Piepla','Paris','Rouge','GrandArena');
INSERT INTO Equipe VALUES('Sabar','Strasbourg','Vert','Boulodrome');
INSERT INTO Equipe VALUES('Direkt','Nancy','Bleu','BukHall');
INSERT INTO Equipe VALUES('Fortiches','Paris','Bleu','GrandArena');

-- /* insertions dans la table Joueur */
INSERT INTO Joueur VALUES('Franck Kou','Direkt',183,22);
INSERT INTO Joueur VALUES('Zhou Zi','Piepla',187,23);
INSERT INTO Joueur VALUES('Manon Messi','Direkt',175,25);
INSERT INTO Joueur VALUES('Aldo Ron','Piepla',174,29);
INSERT INTO Joueur VALUES('Tino Plat','Sabar',189,28);
INSERT INTO Joueur VALUES('Harry Berry','Sabar',183,24);
INSERT INTO Joueur VALUES('Dona Marrat','Direkt',179,25);
INSERT INTO Joueur VALUES('Karl Habruni','Piepla',169,26);
INSERT INTO Joueur VALUES('Jamal Opieh','Direkt',195,25);
INSERT INTO Joueur VALUES('Maurice Filip','Piepla',201,23);
INSERT INTO Joueur VALUES('Fabrice Denice','Sabar',168,22);
INSERT INTO Joueur VALUES('Rico Coco','Sabar',174,21);
INSERT INTO Joueur VALUES('Mario Naite','Fortiches',169,29);
INSERT INTO Joueur VALUES('Chris Tiano','Fortiches',195,28);
INSERT INTO Joueur VALUES('Lino Mockette','Fortiches',201,24);
INSERT INTO Joueur VALUES('Jamal Partu','Fortiches',168,25);

/* insertions dans la table Sponsorise */
INSERT INTO Sponsorise VALUES('Adadis','Franck Kou',156);
INSERT INTO Sponsorise VALUES('Robek','Zhou Zi',265);
INSERT INTO Sponsorise VALUES('Alcampo','Manon Messi',22);
INSERT INTO Sponsorise VALUES('Robek','Aldo Ron',665);
INSERT INTO Sponsorise VALUES('Adadis','Tino Plat',225);
INSERT INTO Sponsorise VALUES('Adadis','Harry Berry',178);
INSERT INTO Sponsorise VALUES('Robek','Dona Marrat',19);
INSERT INTO Sponsorise VALUES('Alcampo','Karl Habruni',164);
INSERT INTO Sponsorise VALUES('Alcampo','Jamal Opieh',542);
INSERT INTO Sponsorise VALUES('Adadis','Maurice Filip',688);
INSERT INTO Sponsorise VALUES('Robek','Fabrice Denice',222);
INSERT INTO Sponsorise VALUES('Carouf','Rico Coco',119);
INSERT INTO Sponsorise VALUES('Carouf','Franck Kou',356);
INSERT INTO Sponsorise VALUES('Adadis','Zhou Zi',228);
INSERT INTO Sponsorise VALUES('Air Monaco','Manon Messi',889);
INSERT INTO Sponsorise VALUES('Adadis','Aldo Ron',865);
INSERT INTO Sponsorise VALUES('Air Monaco','Tino Plat',396);
INSERT INTO Sponsorise VALUES('Carouf','Harry Berry',378);
INSERT INTO Sponsorise VALUES('Alcampo','Dona Marrat',524);
INSERT INTO Sponsorise VALUES('Palasse','Karl Habruni',265);
INSERT INTO Sponsorise VALUES('Palasse','Jamal Opieh',245);
INSERT INTO Sponsorise VALUES('Robek','Maurice Filip',255);
INSERT INTO Sponsorise VALUES('GPS','Fabrice Denice',222);
INSERT INTO Sponsorise VALUES('GPS','Rico Coco',256);

-- /* insertions dans la table Match */
INSERT INTO Match VALUES('Direkt','Piepla','2015-05-12','GrandArena');
INSERT INTO Match VALUES('Direkt','Fortiches','2015-05-13','Boulodrome');
INSERT INTO Match VALUES('Direkt','Sabar','2015-06-15','BukHall');
INSERT INTO Match VALUES('Piepla','Direkt','2015-05-12','GrandArena');
INSERT INTO Match VALUES('Piepla','Fortiches','2015-06-12','Maracanar');
INSERT INTO Match VALUES('Piepla','Sabar','2015-05-15','Maracanar');
INSERT INTO Match VALUES('Sabar','Fortiches','2015-05-12','BukHall');
INSERT INTO Match VALUES('Sabar','Direkt','2015-05-16','BukHall');
INSERT INTO Match VALUES('Sabar','Piepla','2015-05-15','Maracanar');
INSERT INTO Match VALUES('Fortiches','Direkt','2015-05-13','Boulodrome');
INSERT INTO Match VALUES('Fortiches','Piepla','2015-06-12','Maracanar');
INSERT INTO Match VALUES('Fortiches','Sabar','2015-05-12','BukHall');

-- /* insertions dans la table Distance */
INSERT INTO Distance VALUES('GrandArena','Boulodrome',220);
INSERT INTO Distance VALUES('GrandArena','BukHall',30);
INSERT INTO Distance VALUES('GrandArena','Maracanar',124);
INSERT INTO Distance VALUES('Boulodrome','GrandArena',220);
INSERT INTO Distance VALUES('Boulodrome','BukHall',451);
INSERT INTO Distance VALUES('Boulodrome','Maracanar',65);
INSERT INTO Distance VALUES('BukHall','GrandArena',30);
INSERT INTO Distance VALUES('BukHall','Boulodrome',451);
INSERT INTO Distance VALUES('BukHall','Maracanar',180);
INSERT INTO Distance VALUES('Maracanar','GrandArena',124);
INSERT INTO Distance VALUES('Maracanar','Boulodrome',65);
INSERT INTO Distance VALUES('Maracanar','BukHall',180);
