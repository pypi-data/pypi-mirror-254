; ModuleID = 'control_flow_short.ll'
source_filename = "control_flow_short.ll"

%Result = type opaque
%Qubit = type opaque
%String = type opaque

@0 = internal constant [3 x i8] c"()\00"

declare %Result* @__quantum__rt__result_get_one() local_unnamed_addr

declare i1 @__quantum__rt__result_equal(%Result*, %Result*) local_unnamed_addr

declare void @__quantum__rt__result_update_reference_count(%Result*, i32) local_unnamed_addr

declare %Qubit* @__quantum__rt__qubit_allocate() local_unnamed_addr

declare void @__quantum__rt__qubit_release(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare %String* @__quantum__rt__string_create(i8*) local_unnamed_addr

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

define void @control_flow_long__HelloQ() local_unnamed_addr #0 {
entry:
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %0 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %0, label %then0__1.i.i, label %exiting__1.i.i

then0__1.i.i:                                     ; preds = %entry
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %exiting__1.i.i

exiting__1.i.i:                                   ; preds = %then0__1.i.i, %entry
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 1 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %1 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 1 to %Result*))
  br i1 %1, label %then0__1.1.i.i, label %exiting__1.1.i.i

then0__1.1.i.i:                                   ; preds = %exiting__1.i.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %exiting__1.1.i.i

exiting__1.1.i.i:                                 ; preds = %then0__1.1.i.i, %exiting__1.i.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 2 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %2 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 2 to %Result*))
  br i1 %2, label %then0__1.2.i.i, label %exiting__1.2.i.i

then0__1.2.i.i:                                   ; preds = %exiting__1.1.i.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %exiting__1.2.i.i

exiting__1.2.i.i:                                 ; preds = %then0__1.2.i.i, %exiting__1.1.i.i
  tail call void @__quantum__qis__h__body(%Qubit* null)
  tail call void @__quantum__qis__mz__body(%Qubit* null, %Result* nonnull inttoptr (i64 3 to %Result*))
  tail call void @__quantum__qis__reset__body(%Qubit* null)
  %3 = tail call i1 @__quantum__qir__read_result(%Result* nonnull inttoptr (i64 3 to %Result*))
  br i1 %3, label %then0__1.3.i.i, label %control_flow_long__HelloQ__body.1.exit

then0__1.3.i.i:                                   ; preds = %exiting__1.2.i.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  br label %control_flow_long__HelloQ__body.1.exit

control_flow_long__HelloQ__body.1.exit:           ; preds = %exiting__1.2.i.i, %then0__1.3.i.i
  ret void
}

declare void @__quantum__rt__message(%String*) local_unnamed_addr

declare void @__quantum__rt__string_update_reference_count(%String*, i32) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

declare i1 @__quantum__qir__read_result(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="1" }

