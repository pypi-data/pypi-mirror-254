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
  %7 = add i64 %5, 22
  call void @__quantum__rt__int_record_output(i64 %7) 
  br label %fallthrough  
else:
  br label %fallthrough
fallthrough:
  %8 = icmp eq i64 %1, %3
  br i1 %8, label %e_nested_then, label %e_nested_else
e_nested_then:
  br label %exit
e_nested_else:
  %9 = add i64 %5, 6
  ; this branch should be taken
  ; so the corresponding register should have 9
  call void @__quantum__rt__int_record_output(i64 %9) 
  br label %exit
exit:
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
