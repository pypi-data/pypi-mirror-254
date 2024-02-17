; ModuleID = 'measure_only.bc'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  %0 = add i64 1, 2
  %1 = sub i64 2, 2
  ret void
}

; must have requiredresults
attributes #0 = { "EntryPoint" "requiredResults"="1" }
