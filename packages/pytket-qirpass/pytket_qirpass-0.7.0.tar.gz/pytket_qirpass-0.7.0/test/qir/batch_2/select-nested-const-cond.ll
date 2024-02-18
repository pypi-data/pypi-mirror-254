; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = select i1 1, i1 1, i1 0
  br i1 %0, label %then, label %else
then:
  %1 = select i1 1, i64 99, i64 22
  call void @__quantum__rt__integer_record_output(i64 %1)
  br label %exit
else:
  br label %exit
exit:  
  ret void
}

declare void @__quantum__rt__integer_record_output(i64) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
