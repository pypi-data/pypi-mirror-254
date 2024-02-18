; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = icmp eq i32 1, 2
  %1 = icmp ule i32 4, 3
  %2 = icmp ugt i32 4, 2
  %3 = icmp uge i32 5, 1
  %4 = add i32 6, 2
  %5 = add i32 7, 2
  %6 = icmp ult i32 %4, %5
  ret void
}

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }
