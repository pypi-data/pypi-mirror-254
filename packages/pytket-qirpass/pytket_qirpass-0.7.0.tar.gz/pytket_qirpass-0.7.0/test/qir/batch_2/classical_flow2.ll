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
  %4 = sub i64 %1, %3 ; 3
  %5 = icmp ne i64 %1, %4
  br i1 %5, label %then, label %else
then:
  %6 = add i64 %4, 1
  call void @__quantum__rt__int_record_output(i64 %6)
  br label %else
else:  
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
