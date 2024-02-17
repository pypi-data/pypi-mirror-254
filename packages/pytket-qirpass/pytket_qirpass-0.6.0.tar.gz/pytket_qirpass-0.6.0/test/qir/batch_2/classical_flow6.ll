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
  %6 = icmp eq i64 %1, %4
  br i1 %6, label %then, label %else
then:
  %7 = add i64 %5, 1
  %8 = icmp ugt i64 %5, %7
  br i1 %8, label %nested_then, label %nested_else
nested_then:
  br label %exit
nested_else:
  br label %exit
else:
  %9 = add i64 %5, 4
  %10 = icmp ult i64 %9, %5
  br i1 %10, label %e_nested_then, label %e_nested_else
e_nested_then:
  br label %exit
e_nested_else:
  %11 = add i64 %9, 6
  call void @__quantum__rt__int_record_output(i64 %11) ; should be 13
  br label %exit
exit:
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
