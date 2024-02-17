; ModuleID = 'control_flow_complex.ll'
source_filename = "control_flow_complex.ll"

%Qubit = type opaque
%Result = type opaque
%String = type opaque

@0 = internal constant [3 x i8] c"()\00"

declare %Qubit* @__quantum__rt__qubit_allocate() local_unnamed_addr

declare void @__quantum__rt__qubit_release(%Qubit*) local_unnamed_addr

declare %Result* @__quantum__rt__result_get_one() local_unnamed_addr

declare i1 @__quantum__rt__result_equal(%Result*, %Result*) local_unnamed_addr

declare void @__quantum__rt__result_update_reference_count(%Result*, i32) local_unnamed_addr

declare %Result* @__quantum__qis__m__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__reset__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__h__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__x__body(%Qubit*) local_unnamed_addr

declare void @__quantum__qis__z__body(%Qubit*) local_unnamed_addr

declare %String* @__quantum__rt__string_create(i8*) local_unnamed_addr

define void @control_flow_complex__HelloQ() local_unnamed_addr #0 {
entry:
  br label %body__1.i.i

body__1.i.i:                                      ; preds = %continue__1.i.i, %entry
  %i1.i.i = phi i64 [ 0, %entry ], [ %1, %continue__1.i.i ]
  tail call void @__quantum__qis__mz__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*), %Result* null)
  tail call void @__quantum__qis__reset__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  %0 = tail call i1 @__quantum__qir__read_result(%Result* null)
  br i1 %0, label %then0__1.i.i, label %continue__1.i.i

then0__1.i.i:                                     ; preds = %body__1.i.i
  tail call void @__quantum__qis__h__body(%Qubit* nonnull inttoptr (i64 1 to %Qubit*))
  tail call void @__quantum__qis__x__body(%Qubit* null)
  br label %continue__1.i.i

continue__1.i.i:                                  ; preds = %then0__1.i.i, %body__1.i.i
  tail call void @__quantum__qis__z__body(%Qubit* null)
  %1 = add nuw nsw i64 %i1.i.i, 1
  %2 = icmp ult i64 %i1.i.i, 10
  br i1 %2, label %body__1.i.i, label %control_flow_complex__HelloQ__body.1.exit

control_flow_complex__HelloQ__body.1.exit:        ; preds = %continue__1.i.i
  ret void
}

declare void @__quantum__rt__message(%String*) local_unnamed_addr

declare void @__quantum__rt__string_update_reference_count(%String*, i32) local_unnamed_addr

declare void @__quantum__qis__mz__body(%Qubit*, %Result*)

declare i1 @__quantum__qir__read_result(%Result*)

attributes #0 = { "EntryPoint" "requiredQubits"="2" }

