; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @classicalflow() local_unnamed_addr #0 {
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
  %7 = add i64 %5, 1
  %8 = icmp ult i64 %5, %7
  br i1 %8, label %nested_then, label %nested_else
nested_then:
  %9 = add i64 %7, 2
  call void @__quantum__rt__int_record_output(i64 %9) ; should be 6
  br label %else
nested_else:
  br label %else
else:  
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
