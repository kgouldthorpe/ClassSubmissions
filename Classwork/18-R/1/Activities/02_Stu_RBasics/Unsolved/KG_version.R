# Create attendance vector
attendance<-c("Abraham", "Beatrice", "Cory", "Dinah", "Eric", "Felicia")

# Create function to print list with date
print_attendance <- function (list){
  print(Sys.Date())
  for (x in list) {
    print(x)
  }
}
 print_attendance(attendance)

# Create locker combos
locker_combo<-function(list){
  for (x in list){
    combination<-sample(33,3)
    print(x)
    print(combination)
  }
}
locker_combo(attendance)

