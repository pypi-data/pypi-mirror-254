; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = add i1 1, 0
  %1 = select i1 %0, i1 1, i1 0
  br i1 %0, label %then, label %else
then:
  %2 = add i64 4, 5
  %3 = select i1 %1, i64 %2, i64 22
  %4 = add i64 %3, 6
  call void @__quantum__rt__int_record_output(i64 %3)
  call void @__quantum__rt__int_record_output(i64 %4)
  br label %exit
else:
  br label %exit
exit:  
  ret void
}

declare void @__quantum__rt__int_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
