; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @purelyclassical() local_unnamed_addr #0 {
entry:
  %0 = add i64 1, 2 ; 3
  %1 = add i64 %0, 3 ; 6
  %2 = sub i64 4, 2 ; 2
  %3 = add i64 %2, 1 ; 3
  %4 = add i64 %3, %1 ; 9
  %5 = sub i64 %1, %3 ; 3
  %6 = icmp ne i64 %1, %4
  br i1 %6, label %then, label %else
then:
  %7 = icmp ne i64 %2, %4 
  br i1 %7, label %nested_then, label %nested_else
nested_then:
  %8 = add i64 %5, 1; 4
  br label %fallthrough
nested_else:
  %9 = add i64 %5, 2; 5
  br label %fallthrough
else:
  %10 = add i64 %5, 3; 6
  br label %fallthrough
fallthrough:
  %11 = phi i64 [ %8, %nested_then ], [ %9, %nested_else ], [ %10, %else ]	
  %12 = icmp eq i64 %3, %2  
  br i1 %12, label %second_then, label %second_else
second_then:
  %13 = add i64 %4, 1; 10
  br label %exit
second_else:
  %14 = add i64 %4, 2; 11
  br label %exit
exit:  
  %15 = phi i64 [ %13, %second_then ], [ %14, %second_else ]
  call void @__quantum__rt__int_record_output(i64 %11)  
  call void @__quantum__rt__int_record_output(i64 %15)
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
