-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/h9cUic
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Gym" (
    "Gym_id" INT   NOT NULL,
    "Gym_Name" var   NOT NULL,
    "Address" var   NOT NULL,
    "City" var   NOT NULL,
    "Zipcode" var   NOT NULL,
    CONSTRAINT "pk_Gym" PRIMARY KEY (
        "Gym_id"
     )
);

CREATE TABLE "Trainers" (
    "Employee_id" INT   NOT NULL,
    "Gym_id" INT   NOT NULL,
    "First_Name" var   NOT NULL,
    "Last_Name" var   NOT NULL,
    CONSTRAINT "pk_Trainers" PRIMARY KEY (
        "Employee_id"
     )
);

CREATE TABLE "Members" (
    "Member_id" INT   NOT NULL,
    "Gym_id" INT   NOT NULL,
    "First_Name" var   NOT NULL,
    "Last_Name" var   NOT NULL,
    "Address" var   NOT NULL,
    "City" var   NOT NULL,
    CONSTRAINT "pk_Members" PRIMARY KEY (
        "Member_id"
     )
);

CREATE TABLE "Payments" (
    "Member_id" INT   NOT NULL,
    "CreditCard_Info" var   NOT NULL,
    "Billing_Zip" var   NOT NULL,
    CONSTRAINT "pk_Payments" PRIMARY KEY (
        "Member_id"
     )
);

CREATE TABLE "Classes" (
    "Class_id" INT   NOT NULL,
    "Employee_id" Trainers.Employee_id   NOT NULL,
    "Date" var   NOT NULL,
    "Time" var   NOT NULL,
    CONSTRAINT "pk_Classes" PRIMARY KEY (
        "Class_id"
     )
);

ALTER TABLE "Trainers" ADD CONSTRAINT "fk_Trainers_Employee_id" FOREIGN KEY("Employee_id")
REFERENCES "Classes" ("Employee_id");

ALTER TABLE "Trainers" ADD CONSTRAINT "fk_Trainers_Gym_id" FOREIGN KEY("Gym_id")
REFERENCES "Gym" ("Gym_id");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_Member_id" FOREIGN KEY("Member_id")
REFERENCES "Payments" ("Member_id");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_Gym_id" FOREIGN KEY("Gym_id")
REFERENCES "Gym" ("Gym_id");

