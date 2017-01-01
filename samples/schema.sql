drop table if exists SENSORS;
create table SENSORS (
    Id integer primary key autoincrement,
    Unit text,
    Description text
);

drop table if exists DATA;
create table DATA (
  Id integer primary key autoincrement,
  Epoch integer,
  Value real,
  Sensor integer,
  foreign key (Sensor) references SENSORS(Id)
);