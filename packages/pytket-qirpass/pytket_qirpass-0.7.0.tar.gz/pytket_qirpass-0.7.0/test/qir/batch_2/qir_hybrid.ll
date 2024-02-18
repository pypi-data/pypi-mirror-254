; ModuleID = 'qat-link'
source_filename = "qat-link"

%Qubit = type opaque
%Result = type opaque

define void @blackjack_qs__Main__Interop() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %0 = tail call i1 @__quantum__qis__read_result__body(%Result* null)
  br i1 %0, label %then0__1.i, label %blackjack_qs__Main__body.1.exit

then0__1.i:                                       ; preds = %entry
  %1 = tail call i64 @__quantum__qis___hybrid_double__body(i64 2)
  br label %blackjack_qs__Main__body.1.exit

blackjack_qs__Main__body.1.exit:                  ; preds = %entry, %then0__1.i
  ret void
}

declare i64 @__quantum__qis___hybrid_double__body(i64) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*) local_unnamed_addr

declare i1 @__quantum__qis__read_result__body(%Result*) local_unnamed_addr

attributes #0 = { "EntryPoint" "requiredQubits"="1" "requiredResults"="1" }

