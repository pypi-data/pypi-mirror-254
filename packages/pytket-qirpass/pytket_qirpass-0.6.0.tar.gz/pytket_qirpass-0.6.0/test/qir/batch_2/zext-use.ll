; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = or i1 1, 0
  %1 = zext i1 %0 to i64
  %2 = icmp eq i64 %1, 2
  call void @__quantum__rt__bool_record_output(i1 %2)
  ret void
}

declare void @__quantum__rt__bool_record_output(i1) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
